import wikipedia


class Wikipedia():

    def search(self, topic):
        terms = wikipedia.search(topic)[:5]
        message = '<Wikipedia topics>\n'
        message += '\n'.join(terms)
        return message

    def summary(self, topic):
        return wikipedia.summary(topic)

    def content(self, topic):
        page = wikipedia.page(topic)
        return page.content


if __name__ == "__main__":
    wiki = Wikipedia()
    print(wiki.search('code'))
    print(wiki.summary('hackathon'))
