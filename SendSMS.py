from twilio.rest import Client
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class SendSMS():

    def send_sms(self, number, msg_body):
        num = (f'+1{number}')
        client = Client()
        message = client.messages.create(
            to=num, from_="+12059272579", body=msg_body)

if __name__ == "__main__":
    sms_sender = SendSMS()
    body = """
    1. Did you mean "can't" or "cannot"?, ["can't", 'cannot']

    2. Statistics suggests that 'there' (as in 'Is there an answer?') might be the correct word here, not 'their' (as in 'It’s not their fault.'). Please check., ['there']

    3. Possible spelling mistake found, ['we', 'well', 'web']

    4. Possible spelling mistake found, ['because']

    5. Possible spelling mistake found, ['grammar']

    6. Possible spelling mistake found, ['checker', 'cracker']

    7. It's never correct to use 'of' after a modal verb. Use "should have", or, in informal register, "should've"., ['should have', "should've"]

    8. Did you mean "its" (possessive pronoun) instead of 'it's' (=it is)?, ['its']
    """
    numbers = ["6099377475", "6099175688"]
    for number in numbers:
        sms_sender.send_sms(number, body)