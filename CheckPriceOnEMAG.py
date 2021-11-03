# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to alert user of price changes on EMAG


import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import xlwt


now = datetime.now()
time = now.strftime("%d/%m/%Y %H:%M:%S")
print(time)

HEADERS = {"User Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

product_URL = r'https://www.emag.ro/joc-fifa-22-pentru-xbox-one-ea1102701/pd/D7TRFHMBM/'

# Fetch the url
HTML_page = requests.get(product_URL, headers=HEADERS)

# Create the object that will contain all the info in the url
soup = BeautifulSoup(HTML_page.content, "html.parser")

# Get product title
product_title = soup.find("h1", class_="page-title").text.strip()
print(product_title)

# Determine deal status
deal_status = soup.find("p", class_="product-new-price has-deal")
if deal_status is None:
    deal_status = "No deal"
else:
    deal_status = "Has deal"
print(deal_status)

try:
    if("Has deal" in deal_status):
    # to prevent script from crashing when there isn't a price for the product
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

#file_path = input("Please specify the path you want to save in: ")
file_path = r"C:\Users\Me\Desktop"
wb = xlwt.Workbook()
ws = wb.add_sheet("Price_check")
style = xlwt.XFStyle ()   # create a style Object initialization pattern
Al = xlwt.Alignment ()
Al.horz = 0x02       # arranged horizontally centered
Al.vert = 0x01       # set vertical centering
style.alignment = Al

ws.write(0, 0, "Timestamp", style)
ws.write(0, 1, "Product Title", style)
ws.write(0, 2, "Deal Status", style)
ws.write(0, 3, "Product Price", style)
ws.write(1, 0, time, style)
ws.write(1, 1, product_title, style)
ws.write(1, 2, deal_status, style)
ws.write(1, 3, product_price, style)
ws.col(0).width = 256 * 20
ws.col(1).width = 256 * 80
ws.col(2).width = 256 * 12
ws.col(3).width = 256 * 15

wb.save(rf'{file_path}/Price Check.xls')
