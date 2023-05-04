import requests
from bs4 import BeautifulSoup

quote_url = 'http://quotes.toscrape.com/'

response = requests.get(quote_url)

soup = BeautifulSoup(response.content, 'html.parser')


quotes = soup.find_all('span', {'class':'text'})
authors = soup.find_all('small', {'class' : 'author'})
print(authors)
for quote,author in zip(quotes,authors) :
    print(quote.text +" - " + author.text)
