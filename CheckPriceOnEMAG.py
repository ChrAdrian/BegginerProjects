# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to alert user of price changes on EMAG on SMS


import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import xlwt
import time
import os
from xlutils.copy import copy
import xlrd
from twilio.rest import Client
import PySimpleGUI as sg


# product_url = r'https://www.emag.ro/consola-playstation-5-so-9396406/pd/DNKW72MBM/?X-Search-Id=03a182122c656a19adb3&X' \
#               r'-Product-Id=83623105&X-Search-Page=1&X-Search-Position=2&X-Section=search&X-MB=0&X-Search-Action=view'
# file_path = input("Please specify the path you want to save in: ")
# file_path = r"C:\Users\Me\Desktop"
# scan_frequency = input("Please insert scan frequency (in seconds): ")
# file_name = "Price Check"
# file_name = input("Please enter file name: ")
# scan_frequency = 3600
# cycle_number = input("Please insert the number of cycles: ")
# cycle_number = 48
# phone_number = input("Please define phone number (include country code) to receive alerts: ")
# phone_number = "+40754940308"


def current_time():
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    # print(timestamp)
    return timestamp


def get_HTML(product_url):
    HEADERS = {"User Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    # Fetch the url
    HTML_page = requests.get(product_url, headers=HEADERS)
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


def get_base_price(product_price):
    base_price = product_price.replace(" Lei", "")
    base_price = base_price.replace(",", "")
    base_price = base_price.replace(".", "")
    price_change_status = "Base price"
    return base_price, price_change_status


def send_sms(product_url, difference_price, phone_number):
    account_sid = 'AC228e9e6d61c80992890915e6842e5e2c'
    auth_token = '*'
    client = Client(account_sid, auth_token)
    client.messages.create(to=f"{phone_number}",
                           from_="+14327555280",
                           body=f"Price lowered for {get_product_title(get_HTML(product_URL))} "
                                f" with {difference_price} Lei")


def price_change(n, product_price, base_price):
    global price_change_status

    price_change_status = []
    current_price = str(product_price).replace(" Lei", "")
    current_price = str(current_price).replace(",", "")
    current_price = str(current_price).replace(".", "")
    if int(current_price) != int(base_price):
        if int(current_price) > int(base_price):
            difference_price = int(current_price) - int(base_price)
            difference_price = difference_price[::-1]
            difference_price = (difference_price[:2] + ',' + difference_price[2:])[::-1]
            price_change_status = f"Price raised with {difference_price} Lei"
        elif int(current_price) < int(base_price):
            difference_price = int(base_price) - int(current_price)
            difference_price = difference_price[::-1]
            difference_price = (difference_price[:2] + ',' + difference_price[2:])[::-1]
            price_change_status = f"Price lowered with {difference_price} Lei"
            send_sms(product_URL, difference_price, phone_number)
    else:
        price_change_status = f"No price change"

    return price_change_status


def create_output_excel(timestamp, product_title, deal_status, product_price, price_change_status):
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
    ws.write(0, 4, "Price Change", style)
    ws.write(1, 0, timestamp, style)
    ws.write(1, 1, product_title, style)
    ws.write(1, 2, deal_status, style)
    ws.write(1, 3, product_price, style)
    ws.write(1, 4, price_change_status, style)
    ws.col(0).width = 256 * 20
    ws.col(1).width = 256 * 120
    ws.col(2).width = 256 * 12
    ws.col(3).width = 256 * 38
    ws.col(4).width = 256 * 50

    return wb


def save_to_file(file_path, wb, file_name):
    wb.save(rf'{file_path}/{file_name}.xls')


def sleep(sleep_time):
    time.sleep(sleep_time)


def delete_file(file_path, file_name):
    if os.path.isfile(rf'{file_path}/{file_name}.xls'):
        os.remove(rf'{file_path}/{file_name}.xls')


def write_to_existing_file(n, file_path, timestamp, product_title, deal_status, product_price,
                           price_change_status, file_name):
    write_file = xlrd.open_workbook(rf'{file_path}/{file_name}.xls', formatting_info=True)

    wb = copy(write_file)
    ws = wb.get_sheet(0)

    style = xlwt.XFStyle()  # create a style Object initialization pattern
    Al = xlwt.Alignment()
    Al.horz = 0x02  # arranged horizontally centered
    Al.vert = 0x01  # set vertical centering
    style.alignment = Al

    ws.write(int(n + 1), 0, timestamp, style)
    ws.write(int(n + 1), 1, product_title, style)
    ws.write(int(n + 1), 2, deal_status, style)
    ws.write(int(n + 1), 3, product_price, style)
    ws.write(int(n + 1), 4, price_change_status, style)
    ws.col(0).width = 256 * 20
    ws.col(1).width = 256 * 120
    ws.col(2).width = 256 * 12
    ws.col(3).width = 256 * 38
    ws.col(4).width = 256 * 50

    wb.save(rf'{file_path}/{file_name}.xls')


def main_emag(product_url, file_path, file_name, phone_number, scan_frequency, cycle_number):
    global base_price
    n = 1
    timestamp = current_time()
    product_title = get_product_title(get_HTML(product_url))
    deal_status = get_deal_status(get_HTML(product_url))
    product_price = get_product_price(get_HTML(product_url), get_deal_status(get_HTML(product_url)))
    base_price, price_change_status = get_base_price(product_price)
    save_to_file(file_path, create_output_excel(timestamp, product_title, deal_status, product_price,
                                                price_change_status), file_name)
    sleep(int(scan_frequency)*60)

    while n < cycle_number:
        timestamp = current_time()
        product_title = get_product_title(get_HTML(product_url))
        deal_status = get_deal_status(get_HTML(product_url))
        product_price = get_product_price(get_HTML(product_url), get_deal_status(get_HTML(product_url)))
        price_change_status = price_change(n, product_price, base_price)
        write_to_existing_file(n, file_path, timestamp, product_title, deal_status,
                               product_price, price_change_status, file_name)
        n += 1
        sleep(int(scan_frequency)*60)

    exit()


def GUI_main():
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout=[
    [sg.Text('E-market Product Price Checker', size=(30, 1), justification='center', font=("Helvetica", 25),
                relief=sg.RELIEF_RIDGE)],

    [sg.Text('Please enter the product link: '), sg.InputText()],
    [sg.Text('Please select the file save path:   '), sg.InputText(), sg.FolderBrowse()],
    [sg.Text('Please enter the desired file name: '), sg.InputText()],
    [sg.Text('Please enter the phone number in order to receive alerts: '), sg.InputText()],

    [sg.Column([[sg.Text('Please select the scan frequency (minutes)', justification='center')],
    [sg.Slider(range=(1, 60), orientation='h', size=(60, 20), default_value=10)],
    [sg.Text('Please select the number of scanning cycles', justification='center')],
    [sg.Slider(range=(1, 96), orientation='h', size=(60, 20), default_value=6)]])],

    [sg.Button(('OK'), bind_return_key=True), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Password encoder GUI', layout, enable_close_attempted_event=True)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Cancel') \
                and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
            break
        elif event == "OK":
            product_url = values[0]
            file_path = values[1]
            file_name = values[2]
            phone_number = values[3]
            scan_frequency = int(values[4])
            cycle_number = int(values[5])
            main_emag(product_url, file_path, file_name, phone_number, scan_frequency, cycle_number)
            sg.popup(f'File was printed to the following path: {values[1]}')

    window.close()


GUI_main()
# main_emag()
# delete_file(file_path)