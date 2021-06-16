from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def word_frequencies(url):
    """
    Downloads the content from the given URL and returns a dict {word -> frequency}
    giving the count of each word on the page. Ignores HTML tags in the response.
    :param url: Full URL of HTML page
    :return: dict {word -> frequency}
    """
    # open the url (html page)
    html = urlopen(url).read()

    # use beautifulsoup library to process the html
    soup = BeautifulSoup(html)

    # parse the text from html
    for script in soup(["script", "style"]):
        script.decompose()
    strips = list(soup.stripped_strings)

    # regular expression to only take character with letter only from parsed text
    regex = '[a-zA-Z]+'
    result = {}

    # loop each pared text in set of strips so we only loop a set of unique word
    for strip in set(strips):
        # check if the value is a word (contains letter only)
        if re.search(regex, strip):
            word = re.search(regex, strip).group()
            # count the word in the strips array and append it to the result dict
            result[word] = strips.count(strip)
    return result

word_frequencies('https://docs.djangoproject.com/en/3.2/topics/db/aggregation/')
