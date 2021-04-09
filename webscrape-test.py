import requests
from bs4 import BeautifulSoup

URL = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

shop_elems = soup.find_all('div', class_ = 'col-md-9')

for shop_elems in shop_elems:
    items_elem = shop_elems.find('div', class_ = 'row')
    print(items_elem.text)