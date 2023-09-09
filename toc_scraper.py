import requests

res = requests.get("https://katalepsis.net/table-of-contents/")

file = open("table-of-contents.html", "wb")

for chunk in res.iter_content(100000):
    file.write(chunk)
