import translators as ts


class Translate():

    def translate(self, text, dest='en'):
        return ts.google(text, to_language=dest)


if __name__ == "__main__":
    translate = Translate()
    print(translate.translate('hi i like to eat oranges and apples', dest='es'))
