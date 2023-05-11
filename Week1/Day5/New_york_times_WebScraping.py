# import requests
# from bs4 import BeautifulSoup
# import csv

# url = 'https://www.nytimes.com/'
# result = requests.get(url)
# doc = BeautifulSoup(result.content, 'html.parser')

# articles = doc.find_all('article', )
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.nytimes.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('div', class_='css-xdandi')
data = []

for article in articles[:10]:
    title = article.find('h3', class_='css-on971e')#.text.strip()
    description = article.find('p', class_='css-9lwb1u') #.text.strip()
    if title is not None and description is not None:
        data.append({'title': title, 'description': description.text.strip()})

with open('nytimes.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'description'])
    writer.writeheader()
    writer.writerows(data)

print(data)
