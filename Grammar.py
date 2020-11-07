from grammarbot import GrammarBotClient
from dotenv import load_dotenv
import os


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
print(os.environ.get('RAPIDAPI_KEY'))

client = GrammarBotClient(api_key=rapidapi_key)

text = 'I cant remember how to go their'

res = client.check(text)
print(res.matches)
