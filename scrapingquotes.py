import requests
from bs4 import BeautifulSoup
import csv

quote_url = 'http://quotes.toscrape.com/'

response = requests.get(quote_url)

soup = BeautifulSoup(response.content, 'html.parser')


quotes = soup.find_all('span', {'class':'text'})
authors = soup.find_all('small', {'class' : 'author'})

file = open("scraped_quotes.csv","wt")
writer = csv.writer(file)

writer.writerow(["Quotes","Authors"])

for quote,author in zip(quotes,authors) :
    print(quote.text +" - " + author.text)
    writer.writerow([quote.text, author.text])
file.close()
