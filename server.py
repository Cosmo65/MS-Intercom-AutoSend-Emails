from http.server import BaseHTTPRequestHandler, HTTPServer
from intercom.client import Client
import generic
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import string

class HTTPServer_Intercom(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        # Google Spreadsheets Credentials
        scope = ['http://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)

        # Intercom Access Token
        intercom = Client(personal_access_token='dG9rOjU5Nzk3ZGMwXzg3ZTRfNGYwYV9hZjBmXzRhZGI0MmMyYWE1NzoxOjA=')

        # Reset the Applicants in a worksheet of a Google Spreadsheet document
        spreadsheet_title = input("Title of your spreadsheet (e.g. Fall 2018 Regular Decision Challenge QA): ")
        worksheet_title = input("Title of your worksheet: ")
        admin_name = input("What's your Intercom name? ")
        sheet = client.open(spreadsheet_title).worksheet(worksheet_title)

        result = sheet.get_all_records()
        for row, applicant in enumerate(result):
            if applicant.get("Admin Action Taken", "None") != "None" and applicant.get("Emailed?", "Yes") in (
            "No", "no"):
                # reset each applicant
                applicant_email = applicant.get("Email")
                try:
                    user = intercom.users.find(email=applicant_email)

                    reason = applicant.get("Reason to Reset")

                    actions = applicant.get("Admin Action Taken", "").split(" ")
                    translator = str.maketrans('', '', string.punctuation)
                    actions = [action.translate(translator) for action in actions]
                    to_reset = {
                        "Understanding": False,
                        "Writing": False,
                        "Math": False,
                        "Creativity": False,
                        "Reasoning": False
                    }
                    for action in actions:
                        if action in to_reset:
                            to_reset[action] = True


                    for challenge in to_reset:
                        if to_reset[challenge] is True:
                            msg = generic.GenericChallengeReset(admin=admin_name, challenge=challenge,
                                                                reason=reason)
                            subject, body = msg.response()["subject"], msg.response()["body"]
                            email = intercom.messages.create(**{
                                "message_type": "email",
                                "subject": subject,
                                "body": body,
                                "template": "plain",
                                "from": {
                                    "type": "admin",
                                    "id": "1482390"
                                },
                                "to": {
                                    "type": "user",
                                    "id": user.id
                                }
                            })

                    sheet.update_acell('K{}'.format(row+2), 'Yes')

                    print("{} is notified about the reset.".format(applicant_email))

                except:
                    message = sys.exc_info()[1]
                    print(message)
                    print("Please make sure that the email \"{}\" is registered on Intercom".format(email))


    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        pass


def run_server():
    print("Starting server http://127.0.0.1:8080/...")

    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, HTTPServer_Intercom)
    print("Running server http://127.0.0.1:8080/...")
    httpd.serve_forever()


run_server()
