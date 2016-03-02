import re
import urllib.request
from bs4 import BeautifulSoup

wishlist = '108CUW1LYHCYJ'
amazon_url = 'http://www.amazon.ca/registry/wishlist/'

url = amazon_url + wishlist

request = urllib.request.urlopen(url)

# if request.code == 200:
raw_html = request.read()

soup = BeautifulSoup(raw_html, 'lxml')

items = soup.find_all('div', {'id':re.compile("item_\S+")})

for item in items:

    id_string = item.attrs['id']

    id = id_string[id_string.find('_')+1:]
    title = item.find('a', {'id':'itemName_{id}'.format(id=id)}).attrs['title']

    item.find('span', {'id':'itemPrice_{id}'.format(id=id)}).contents
    
    print(id, title)

    


id_start = item_id.index('_') + 1

item_id[id_start:]




