import requests
import bs4
import re

toc = open("table-of-contents.html", "r")

soup = bs4.BeautifulSoup(toc, "html.parser")

links = []

for link in soup.find_all("a", attrs={"href": re.compile("^https://")}):
    links.append(link.get("href"))

i = 1

for chapterlink in links:
    res = requests.get(chapterlink)
    res.raise_for_status()
    testSoup = bs4.BeautifulSoup(res.text, "html.parser")

    content = testSoup.select(".entry-content")
    content_str = str(content)

    chapter_name = f"Chapter{i}.html"
    i += 1
    contentfile = open(chapter_name, "wb")

    links = testSoup.find_all("a")

    contentfile.write(content_str.encode())
