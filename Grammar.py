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
        message = ''
        res = self.client.check(text)
        for i, match in enumerate(res.matches):
            message += f'\n{i+1}. {match.message}, {match.replacements[:3]}\n'
        return message


if __name__ == "__main__":
    grammar = Grammar()
    print(grammar.check(
        'I cant remember how to go their. I hope your doing wel, becaues this grmmar chrkcker should of done it\'s job'))
    print(grammar.check(
        'i relly loce koding and there are so many exziting ebents'))
