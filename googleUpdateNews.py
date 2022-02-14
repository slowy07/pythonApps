import ssl
from urllib.request import urlopen

"""
for information about beautifulsoup or how to install check on:
https://pypi.org/project/beautifulsoup4/
"""

from bs4 import BeautifulSoup as soup


def news(xmlNewsUrl, counter):
    context = ssl._create_unverified_context()
    client = urlopen(xmlNewsUrl, context=context)
    xmlPage = client.read()
    client.close()

    soupPage = soup(xmlPage, "xml")
    newsList = soupPage.findAll("item")
    i = 0

    for news in newsList:
        print(f"news title:   {news.title.text}")  # to print title of the news
        print(f"news link:    {news.link.text}")  # to print link of the news
        print(f"news pubDate: {news.pubDate.text}")  # to print published date

        print("+-" * 20, "\n\n")

        if i == counter:
            break
        else:
            i = i + 1


newsUrl = "https://news.google.com/news/rss/?ned=us&gl=US&hl=en"
sportUrl = "https://news.google.com/news/rss/headlines/section/topic/SPORTS.en_in/Sports?ned=in&hl=en-IN&gl=IN"

# print news
news(newsUrl, 10)
news(sportUrl, 5)
