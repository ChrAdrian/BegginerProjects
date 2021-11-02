# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to alert user of price changes on EMAG


import requests
from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep


HEADERS = {"User Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

prod_tracker_URL = r'https://www.emag.ro/espressor-automat-miele-cm-6160-milkperfection-white-15-bar-1-8-l-' \
                   'wificonnatct-onetouch-for-two-aromaticsystem-alb-11580780/pd/D84HT2MBM/?X-' \
                   'Search-Id=0357319c0c5d3a33c2dc&X-Product-Id=7108689&X-Search-Page=1&X-Search-Position=2&X-' \
                   'Section=search&X-MB=0&X-Search-Action=view'

# fetch the url
page = requests.get(prod_tracker_URL, headers=HEADERS)

# create the object that will contain all the info in the url
soup = BeautifulSoup(page.content, "html.parser")
