
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.nytimes.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('div', class_='css-xdandi')
data = []


with open('nytimes.csv', 'w', newline='') as csv_file:
    # writer = csv.DictWriter(file, fieldnames=['title', 'description'])
    # writer.writeheader()
    # writer.writerows(data)
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['title', "description"])

    for article in articles[:10]:
        title = article.find('h3', class_='css-on971e')  # .text.strip()
        description = article.find('p', class_='css-9lwb1u')  # .text.strip()
        if title is not None and description is not None:
            data.append(
                {'title': title, 'description': description.text.strip()})
        print(article)

        csv_writer.writerow([title, description])
