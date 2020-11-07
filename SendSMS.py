from twilio.rest import Client
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

client = Client()
message = client.messages.create(to="+16099377475",from_="+12059272579",body="Test MSG")