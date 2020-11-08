from twilio.rest import Client
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class SendSMS():

    def send_sms(self, number, msg_body):
        if len(msg_body) == 0:
            return False
        num = (f'+1{number}')
        client = Client()
        message = client.messages.create(
            to=num, from_="+12059272579", body=msg_body)
        return True

if __name__ == "__main__":
    sms_sender = SendSMS()
    numbers = ["6099377475", "6099175688"]
    for number in numbers:
        sms_sender.send_sms(number, "poop")