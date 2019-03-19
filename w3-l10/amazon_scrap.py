#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

# set the headers to avoid bot restrictions
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.56 Safari/537.36'}

# set the URL to fetch
url = "https://www.amazon.com/s?k=horse+head+mask"

# craft the page query (URL + Headers)
response = requests.get(url, headers=headers)

# Run the response through BeautifulSoup to clean it up.
soup = BeautifulSoup(response.text, "html.parser")

# Look for the the X divs with class ID Y and return as a list.
results = soup.find_all('div', {'class' : 'sg-col-inner'})

amazonResults = {}
for result in results:
    title = result.find('span', {'class' : 'a-size-base-plus a-color-base a-text-normal'})
    if title != None:
        amazonResults[title.get_text()] = ''
    price = result.find('span', {'class' : 'a-offscreen'})
    if price != None and title != None:
        amazonResults[title.get_text()] = price.get_text()

for k,v in amazonResults.items():
    print(f"{k} : {v}")
