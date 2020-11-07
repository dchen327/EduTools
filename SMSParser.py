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
        features = ['help', 'wiki', 'translate', 'grammar', 'mathpix']
        try:
            feature = sections[0]
            if feature not in features:
                return 'Feature not found'
            elif feature == 'help':
                return self.commands()
            elif feature == 'wiki':
                action = sections[1]
                wiki_actions = ['search', 'summary', 'content']
                if action not in wiki_actions:
                    return 'Action not found'
                text = ' '.join(sections[2:])
                return getattr(self.wiki, action)(text)
            elif feature == 'translate':
                dest_lang = sections[1]
                text = ' '.join(sections[2:])
                return self.translate.translate(text, dest=dest_lang)
            elif feature == 'mathpix':
                pass
            elif feature == 'grammar':
                text = ' '.join(sections[1:])
                print(text)
                return self.grammar.check(text)
        except:
            return 'Something went wrong. Please double-check your command!'


if __name__ == "__main__":
    sms_parser = SMSParser()
    command = 'translate en me gusta mucho comer las manzanas'
    command = 'help'
    print(sms_parser.parse(command))
