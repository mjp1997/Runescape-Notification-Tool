# import necessary libraries/modules
from bs4 import BeautifulSoup
import requests
import csv

# hello
# get requests from the osrs website
source = requests.get("http://oldschool.runescape.com").text
soup = BeautifulSoup(source, "lxml")

osrsOutput = open("osrsOutput.txt", "w")
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(["headline", "summary", "video_link"])

# print the necessary components of all recent updates
for article in soup.find_all("article"):

    headline = article.h3.a.text
    osrsOutput.write(headline + "\n")
    print(headline)

    summary = article.find("div", class_="news-article__details").p.text
    osrsOutput.write(summary + "\n")
    print(summary)

    updateLink = article.find("div", class_="news-article__details").p.a
    updateLink = str(updateLink)
    hrefStart = updateLink.find("https://secure")
    print(type(updateLink))
    newHalfLink = updateLink[hrefStart:-1]
    secondHalfLink = newHalfLink.split('"')[0]
    osrsOutput.write(secondHalfLink + "\n")
    print(secondHalfLink)

    print()

