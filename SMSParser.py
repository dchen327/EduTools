from MathSolver import MathSolver
from Wikipedia import Wikipedia
from Translator import Translate
from Grammar import Grammar
from inspect import cleandoc
import time


class SMSParser():

    def __init__(self):
        self.wiki = Wikipedia()
        self.translate = Translate()
        self.grammar = Grammar()
        self.math_solver = MathSolver()

    def commands(self):
        commands = '''List of commands:
        1. commands
        2. wiki <search/summary/content> <topic>
        3. translate <dest lang abbrev.> <text>
        4. grammar <text>
        5. mathpix <img> (image in new sms)
        6. duesoon
        '''
        return cleandoc(commands)

    def parse(self, text):
        # add some placeholders for error handling
        sections = text.strip().split() + [''] * 2
        features = ['commands', 'wiki', 'translate', 'grammar', 'mathpix', 'duesoon']
        try:
            feature = sections[0]
            if feature not in features:
                return 'Feature not found'
            elif feature == 'commands':
                return self.commands()
            elif feature == 'wiki':
                action = sections[1]
                wiki_actions = ['search', 'summary', 'content']
                if action not in wiki_actions:
                    return 'Action not found'
                text = ' '.join(sections[2:])
                print(text)
                print(self.wiki.summary(text))
                return getattr(self.wiki, action)(text)
            elif feature == 'translate':
                dest_lang = sections[1]
                text = ' '.join(sections[2:])
                return self.translate.translate(text, dest=dest_lang)
            elif feature == 'mathpix':
                equation = self.math_solver.read_math('test1.jpg')
                return self.math_solver.solve_math2("find zeroes for:" + equation)
            elif feature == 'grammar':
                text = ' '.join(sections[1:])
                return self.grammar.check(text)
            elif feature == "duesoon":
                time.sleep(4)
                return('Upcoming due dates:\n\n14.4 Problem Set - Due in 2 day(s)\n\nHemingway Reading Questions - Due in 1 day(s)')
        except Exception as e:
            print(e)
            return 'Something went wrong. Please double-check your command!'


if __name__ == "__main__":
    sms_parser = SMSParser()
    command = 'translate en me gusta mucho comer las manzanas'
    command = 'mathpix 2+3'
    print(sms_parser.parse(command))
