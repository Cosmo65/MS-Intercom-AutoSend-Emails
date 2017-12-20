from intercom.client import Client
intercom = Client(personal_access_token='dG9rOjU5Nzk3ZGMwXzg3ZTRfNGYwYV9hZjBmXzRhZGI0MmMyYWE1NzoxOjA=')
user = intercom.users.find(email = raw_input("Email: "))

email = intercom.messages.create(**{
    "message_type": "email",
    "subject": "Using Python",
    "body": "Calling API Test3 :)",
    "template": "plain", # or "personal",
    "from": {
        "type": "admin",
        "id": "1482390"
    },
    "to": {
        "type": "user",
        "id": user.id
    }
})

print(email)