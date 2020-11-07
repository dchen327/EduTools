from grammarbot import GrammarBotClient
from dotenv import load_dotenv
import os


class Grammar():

    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        rapidapi_key = os.environ.get('RAPIDAPI_KEY')
        self.client = GrammarBotClient(api_key=rapidapi_key)

    def check(self, text):
        res = self.client.check(text)
        return res.matches


if __name__ == "__main__":
    grammar = Grammar()
    print(grammar.check('I cant remember how to go their'))
