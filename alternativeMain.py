import requests
from bs4 import BeautifulSoup
import json


def crawling(arg1):
    URL = "https://www.reddit.com/search/?q=%s"
    outfile = open('result2.json', 'w')
    if arg1:
        URL = URL % arg1
        print(URL)
    r = requests.get(URL)

    soup = BeautifulSoup(r.content,
                         "html.parser")
    attrs = {'class': "_2SdHzo12ISmrC8H86TgSCp _1zpZYP8cFNLfLDexPY65Y7 ", }
    post_list = soup.find_all("div", {"class": "_1poyrkZ7g36PawDueRza-J"})
    title = []
    comments = None
    upvotes = None
    if post_list:
        print("var")
    for post in post_list:
        # print(post.text)
        for span in post.find_all("span", {"class": "_vaFo96phV6L5Hltvwcox"}):
            if "upvotes" in span.text:
                upvotes = span.text
                # print(span.text)
            if "comments" in span.text:
                comments = span.text
                # print(span.text)
            data = {
                'counts_comment': str(comments).split('comments')[0],
                'score': str(upvotes).split('upvotes')[0],
                'title': post.find('h3').text,
                # 'selftext': post.selftext,
            }
        print(data)

        json.dump(data, outfile)
        # print(soup.prettify())


print("Enter a word for reddit seaching:")
arg1 = str(input())
crawling(arg1)