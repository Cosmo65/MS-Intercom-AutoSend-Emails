from intercom.client import Client

import generic

intercom = Client(personal_access_token='dG9rOjU5Nzk3ZGMwXzg3ZTRfNGYwYV9hZjBmXzRhZGI0MmMyYWE1NzoxOjA=')
user = intercom.users.find(email=raw_input("Email: "))

msg = generic.GenericChallengeReset(admin="Yong", challenge="Expression", reason="your internet connection is terrible.")
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

print(email)
