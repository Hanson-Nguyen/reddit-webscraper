import requests
from bs4 import BeautifulSoup

URL = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

shop_elems = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')

for item_elems in shop_elems:

    items_name = item_elems.a.text
    items_cost = item_elems.h4.text
    items_desc = item_elems.p.text

    rating_div = item_elems.find('div', {'class': 'ratings'})
    rating_tag = rating_div.find('p')

    items_reviews = rating_tag.text

    print(items_name)
    print(items_cost)
    print(items_desc)
    print(items_reviews)
    print()

#print(items_stars + " stars")