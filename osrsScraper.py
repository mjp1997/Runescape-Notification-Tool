# import necessary libraries/modules
from bs4 import BeautifulSoup
import requests
import csv

# hello
# get requests from the osrs website
source = requests.get("http://oldschool.runescape.com").text
soup = BeautifulSoup(source, "lxml")

# csv_file = open("cms_scrape.csv", "w")
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(["headline", "summary", "video_link"])

# print the necessary components of all recent updates
for article in soup.find_all("article"):

    headline = article.h3.a.text
    print(headline)

    summary = article.find("div", class_="news-article__details").p.text
    print(summary)

    updateLink = article.find("div", class_="news-article__details").p.a
    updateLink = str(updateLink)
    hrefStart = updateLink.find("https://secure")
    print(type(updateLink))
    newHalfLink = updateLink[hrefStart:-1]
    secondHalfLink = newHalfLink.split('"')[0]
    print(secondHalfLink)

    print()

