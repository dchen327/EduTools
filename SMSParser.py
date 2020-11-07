from Wikipedia import Wikipedia
from Translator import Translate
from Grammar import Grammar
from inspect import cleandoc


class SMSParser():

    def __init__(self):
        self.wiki = Wikipedia()
        self.translate = Translate()
        self.grammar = Grammar()

    def commands(self):
        commands = '''List of commands:
        1. help
        2. wiki <search/summary/content> <topic>
        3. translate <dest lang abbrev.> <text>
        4. grammar <text>
        5. mathpix <img> (image in new sms)
        '''
        return cleandoc(commands)

    def parse(self, text):
        # add some placeholders for error handling
        sections = text.strip().split() + [''] * 2
        features = ['wiki', 'translate', 'grammar', 'mathpix']
        feature = sections[0]
        if feature not in features:
            return 'Feature not found'
        if feature == 'wiki':
            action = sections[1]
            wiki_actions = ['search', 'summary', 'content']
            if action not in wiki_actions:
                return 'Action not found'
            text = sections[2]
            return getattr(self.wiki, action)(text)
        elif feature == 'translate':
            pass
        elif feature == 'mathpix':
            pass
        elif feature == 'grammar':
            pass


if __name__ == "__main__":
    sms_parser = SMSParser()
    print(sms_parser.commands())
    command = '''wiki search Python'''
    print(sms_parser.parse(command))
