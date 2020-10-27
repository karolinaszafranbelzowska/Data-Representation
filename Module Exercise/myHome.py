


import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.myhome.ie/residential/mayo/property-for-sale?page=1"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

home_file = open('week03MyHome.csv', mode='w')
home_writer =csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="PropertyListingCard")

for listing in listings:
    entryL = []

    price = listing.find(class_="PropertyListingCard__Price").text
    entryL.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entryL.append(address)

    home_writer.writerow(entryL)
home_file.close()
