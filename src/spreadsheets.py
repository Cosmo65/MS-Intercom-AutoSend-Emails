import gspread
from oauth2client.service_account import ServiceAccountCredentials
import string

scope = ['http://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

worksheet_title = input("Title of your worksheet: ")
sheet = client.open('Fall 2018 Regular Decision Challenge QA').worksheet(worksheet_title)

result = sheet.get_all_records()
for applicant in result:
    if applicant.get("Admin Action Taken", "None") != "None" and applicant.get("Emailed?", "Yes") in ("No", "no"):
        email = applicant.get("Email")
        actions = applicant.get("Admin Action Taken","").split(" ")
        translator = str.maketrans('', '', string.punctuation)
        actions = [action.translate(translator) for action in actions]

        to_reset = {
            "Understanding": False,
            "Writing" : False,
            "Math": False,
            "Creativity": False,
            "Reasoning": False
        }

        for action in actions:
            if action in to_reset:
                to_reset[action] = True

        reason = applicant.get("Reason to Reset")

        print(email, to_reset)




# Methods
# .row_values(row_number)
# .col_values(col_number)
# .cell(row, col).value
# .update_cell(row, col, new_value)
# .insert_row(array, row_num)
# .delete_row(row_num)