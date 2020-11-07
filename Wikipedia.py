import wikipedia


class Wikipedia():

    def search(self, search_term):
        terms = wikipedia.search(search_term)[:5]
        message = '<Wikipedia topics>\n'
        message += '\n'.join(terms)
        return message

    def summary(self, topic):
        return wikipedia.summary(topic)


if __name__ == "__main__":
    wiki = Wikipedia()
    print(wiki.search('code'))
