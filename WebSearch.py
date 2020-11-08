from search_engine_parser.core.engines.google import Search as GoogleSearch
from Wikipedia import Wikipedia
from Translator import Translate
from Grammar import Grammar
from inspect import cleandoc
import asyncio
from pyppeteer import launch
class WebSearch():
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
        6. google <query> 
        '''
        return cleandoc(commands)
    async def search(self, query):
        gresults = gsearch.search(*query)
        browser = await launch(headless=True)
        page = await browser.newPage()
        await page.goto(gresults["links"][0])
        await page.screenshot({'/Users/rohit/Documents/pics': 'screen.png', 'fullPage': True}) #temp path
        await browser.close()
if __name__ == "__main__":
    web_search = WebSearch()
    print(web_search.commands())
    query = '''election results'''
    print(web_search.search(query))
