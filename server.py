from http.server import BaseHTTPRequestHandler, HTTPServer
from intercom.client import Client
import generic
import sys

class HTTPServer_Intercom(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text')
		self.end_headers()

	def do_GET(self):
		self._set_headers()
		intercom = Client(personal_access_token='dG9rOjU5Nzk3ZGMwXzg3ZTRfNGYwYV9hZjBmXzRhZGI0MmMyYWE1NzoxOjA=')

		confirmed = False
		while not confirmed:
			while True:
				try:
					email = input("Email: ")
					user = intercom.users.find(email=email)
					break
				except:
					message = sys.exc_info()[1]
					print(message)
					print("Please make sure that the email \"{}\" is correct".format(email))
			admin_name = input("Your Name (Not the Applicant's Name): ")
			challenge = input("Challenge that is reset: ")
			reason = input("Reason for resetting (don't start with capital letter): ")
			msg = generic.GenericChallengeReset(admin=admin_name, challenge=challenge,
												reason=reason)
			subject, body = msg.response()["subject"], msg.response()["body"]

			print('\nMessage to be sent: \n===================')
			print(subject)
			print(body)

			confirmed_response = input("Is this the message you want? Type 'Y' if yes, 'N' if no \nResponse: ")
			if confirmed_response == 'Y':
				confirmed = True

		print("Message sending...")
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

		if email:
			print("Success\n\n")

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
