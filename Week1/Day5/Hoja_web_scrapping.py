# Webscrapping from a Hojaleaks 

from bs4 import BeautifulSoup
import requests
import csv

url = "https://hojaleaks.com/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

headings = doc.find_all("h1")
summaries = doc.find_all("p", class_="css-ko0c54")
# parent = headings[0].parent
# a = parent.find_all("a")
# print(a)
for heading in headings:
    print(heading.text)

for summary in summaries:
    print(summary.text)

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Heading', 'Summary'])

    for heading, summary in zip(headings, summaries):
        writer.writerow([heading.text, summary.text])

