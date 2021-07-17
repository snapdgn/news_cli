#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import csv
from prettytable import from_csv
page = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(page.content, 'html.parser')

top_items = []

content = soup.find_all("tr", {"class": "athing"})


for items in content:
    article = items.select('a.storylink')[0].text
    links = items.find_all('a',class_ = 'storylink')

    for link in links:
        link_url = link["href"]
    info = {
            "title":article.strip(),
            "href":link_url.strip()
            }
    top_items.append(info)

# print(top_items)

keys = top_items[0].keys()

with open('news.csv','w', newline = '') as outfile:
     writer = csv.DictWriter(outfile, keys)
     writer.writeheader()
     writer.writerows(top_items)

with open("news.csv", "r") as fp:
    x = from_csv(fp)

# x.set_style(DEFAULT)
print(x)
