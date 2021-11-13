# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to fetch Covid informations by Country


from bs4 import BeautifulSoup
import requests


# country = input("Please insert country to fetch data for: ")
page = requests.get("https://www.worldometers.info/coronavirus/")
html = page.text
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table", attrs={"id":"main_table_countries_today"})
print(table)