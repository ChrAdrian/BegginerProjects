# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to alert user of price changes on EMAG


import requests
from bs4 import BeautifulSoup
import re


HEADERS = {"User Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

product_URL = r'https://www.emag.ro/consola-playstation-5-so-9396406/pd/DNKW72MBM/'

# Fetch the url
HTML_page = requests.get(product_URL, headers=HEADERS)

# Create the object that will contain all the info in the url
soup = BeautifulSoup(HTML_page.content, "html.parser")

# Get product title
product_title = str(soup.product_title).strip('<title>')
product_title = re.sub(" - eMAG.ro</", "", product_title)

# Determine deal status
deal_status = soup.find("p", class_="product-new-price has-deal")
if deal_status is None:
    deal_status = "No deal"
else:
    deal_status = "Has deal"

try:
    if("Has deal" in deal_status):
        product_price = soup.find("p", class_="product-new-price has-deal").text
        product_price = product_price[::-1]
        product_price = (product_price[:6] + ',' + product_price[6:])[::-1]
    else:
        product_price = soup.find("p", class_="product-new-price").text
        product_price = product_price[::-1]
        product_price = (product_price[:6] + ',' + product_price[6:])[::-1]
except:
    product_price = 'No price is assigned to this product'


print(product_price)

