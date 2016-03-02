import re
import urllib.request
from bs4 import BeautifulSoup


WISHLIST_URL = 'http://www.amazon.ca/registry/wishlist/'

wishlist_id = '108CUW1LYHCYJ'


def get_wishlist_items(wishlist_id):
    ''' Gets the ASIN item identifier of all items in wishlist '''

    wishlist_items = []

    url = WISHLIST_URL + wishlist_id
    request = urllib.request.urlopen(url)

    if request.code == 200:
        raw_html = request.read()

        soup = BeautifulSoup(raw_html, 'lxml')

        items = soup.find_all('div', {'id': re.compile("item_\S+")})

        for item in items:

            id_string = item.attrs['id']
            asin = id_string[id_string.find('_')+1:]

            wishlist_items.append(asin)

    return wishlist_items

get_wishlist_items(wishlist_id)

'''
title = item.find('a', {'id': 'itemName_'}).attrs['title']

p = item.find('span', {'id': 'itemPrice_'})

print(id, title, price_string)
'''
