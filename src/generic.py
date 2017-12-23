class GenericChallengeReset:
    def __init__(self, admin, challenge, reason):
        self.data = {"challenge": challenge, "admin": admin, "reason": reason}

    def response(self):
        subject = "[Action Required] Reset Minerva {challenge} Challenge".format(**self.data)
        body = "As part of a regular quality check, I noticed a problem with your {challenge} challenge. In particular, {reason} I've reset that challenge for you. \nPlease return to your Admission Center (https://www.minerva.kgi.edu/application/admission-center/) to take the challenge again to be considered for Minerva. \nBefore starting, please confirm that your camera and microphone are functional. You can reply to this message if you have any questions. \n\nThanks, \n{admin}".format(
            **self.data)
        return {"subject": subject, "body": body}
