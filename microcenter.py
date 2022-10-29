import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get('https://www.microcenter.com/brand/4294818256/raspberry-pi')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# print pretty
print(soup.prettify())


# get item name for each available product
inventory = soup.find_all('div', class_='pDescription compressedNormal3')
inventory = []
for i in inventory:
    inv = i.text
    inv = i.strip()
    inv= i.replace('\n', '')
    inv = i.replace(' ', '')
    inventory.append(inv)
len(inventory)
print(inventory)


inventory_status_message = soup.find_all('span', class_='msgInStock')
inventory_status_message = []
for i in inventory_status_message:
    inv = i.text
    inv = i.strip()
    inv= i.replace('\n', '')
    inv = i.replace(' ', '')
    inventory_status_message.append(inv)
len(inventory_status_message)
print(inventory_status_message)

inventory_count = soup.find_all('span', class_='inventoryCNT')
inventory_count = []
for i in inventory_count:
    inv = i.text
    inv = i.strip()
    inv= i.replace('\n', '')
    inv = i.replace(' ', '')
    inventory_count.append(inv)
len(inventory_count)
print(inventory_count)





list1 = inventory
list2 = inventory_count
list3 = inventory_status_message

# create dictionary
dictionary = {'item': list1, 'count': list2, 'message': list3}

## put this together into a dataframe
df = pd.DataFrame({'item':inventory,'count':inventory_count, 'message':inventory_status_message})

df.to_csv('web-scraping/data/microcenter.csv')