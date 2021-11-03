# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to alert user of price changes on EMAG


import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import xlwt
import time
import os
from xlutils.copy import copy
import xlrd


product_URL = r'https://www.emag.ro/telefon-mobil-apple-iphone-12-pro-max-128gb-5g-pacific-blue-mgda3rm-a/pd/DDWRH7MBM/'
# file_path = input("Please specify the path you want to save in: ")
file_path = r"C:\Users\Me\Desktop"


def current_time():
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    # print(timestamp)
    return timestamp


def get_HTML(product_url):
    HEADERS = {"User Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    # Fetch the url
    HTML_page = requests.get(product_URL, headers=HEADERS)
    # Create the object that will contain all the info in the url
    soup = BeautifulSoup(HTML_page.content, "html.parser")
    return soup


def get_product_title(soup):
    # Get product title
    product_title = soup.find("h1", class_="page-title").text.strip()
    # print(product_title)
    return product_title


def get_deal_status(soup):
    # Determine deal status
    deal_status = soup.find("p", class_="product-new-price has-deal")
    if deal_status is None:
        deal_status = "No deal"
    else:
        deal_status = "Has deal"
    # print(deal_status)
    return deal_status


def get_product_price(soup, deal_status):
    try:
        if "Has deal" in deal_status:
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
    # print(product_price)
    return product_price


def create_output_excel(timestamp, product_title, deal_status, product_price):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Price_check")

    style = xlwt.XFStyle()  # create a style Object initialization pattern
    Al = xlwt.Alignment()
    Al.horz = 0x02  # arranged horizontally centered
    Al.vert = 0x01  # set vertical centering
    style.alignment = Al

    ws.write(0, 0, "Timestamp", style)
    ws.write(0, 1, "Product Title", style)
    ws.write(0, 2, "Deal Status", style)
    ws.write(0, 3, "Product Price", style)
    ws.write(1, 0, timestamp, style)
    ws.write(1, 1, product_title, style)
    ws.write(1, 2, deal_status, style)
    ws.write(1, 3, product_price, style)
    ws.col(0).width = 256 * 20
    ws.col(1).width = 256 * 80
    ws.col(2).width = 256 * 12
    ws.col(3).width = 256 * 38

    return wb


def save_to_file(file_path, wb):
    wb.save(rf'{file_path}/Price Check.xls')


def sleep(sleep_time):
    time.sleep(sleep_time)


def delete_file(file_path):
    if os.path.isfile(rf'{file_path}/Price Check.xls'):
        os.remove(rf'{file_path}/Price Check.xls')


def write_to_existing_file(n, file_path, timestamp, product_title, deal_status, product_price):
    write_file = xlrd.open_workbook(rf'{file_path}/Price Check.xls', formatting_info=True)

    wb = copy(write_file)
    ws = wb.get_sheet(0)

    style = xlwt.XFStyle()  # create a style Object initialization pattern
    Al = xlwt.Alignment()
    Al.horz = 0x02  # arranged horizontally centered
    Al.vert = 0x01  # set vertical centering
    style.alignment = Al

    ws.write(int(n + 2), 0, timestamp, style)
    ws.write(int(n + 2), 1, product_title, style)
    ws.write(int(n + 2), 2, deal_status, style)
    ws.write(int(n + 2), 3, product_price, style)
    ws.col(0).width = 256 * 20
    ws.col(1).width = 256 * 80
    ws.col(2).width = 256 * 12
    ws.col(3).width = 256 * 38

    wb.save(rf'{file_path}/Price Check.xls')


def main():
    timestamp = current_time()
    product_title = get_product_title(get_HTML(product_URL))
    deal_status = get_deal_status(get_HTML(product_URL))
    product_price = get_product_price(get_HTML(product_URL), get_deal_status(get_HTML(product_URL)))
    save_to_file(file_path, create_output_excel(timestamp, product_title, deal_status, product_price))
    sleep(60)
    n = 0
    while n < 50:
        timestamp = current_time()
        product_title = get_product_title(get_HTML(product_URL))
        deal_status = get_deal_status(get_HTML(product_URL))
        product_price = get_product_price(get_HTML(product_URL), get_deal_status(get_HTML(product_URL)))
        write_to_existing_file(n, file_path, timestamp, product_title, deal_status, product_price)
        n += 1
        sleep(60)

    exit()


main()
# delete_file(file_path)
