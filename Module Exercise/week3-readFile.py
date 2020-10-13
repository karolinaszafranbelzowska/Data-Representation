import requests
from bs4 import BeautifulSoup

# Read File from requests.get

page = requests.get("https://raw.githubusercontent.com/karolinaszafranbelzowska/Data-Representation/main/Lab/carviewer2.html")

print(page)
print(".................")
print(page.content)

soup1 = BeautifulSoup(page.content,'html.parser')
print(soup1.prettify())


# Read File from with open

with open("../Lab/carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print(soup.prettify())





