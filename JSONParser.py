# Script created by Chiriac Adrian Stefan (adrian.chiriac@tremend.com)
# Brief : script to parse JSON file


import json
import os


os.chdir(r"C:\Users\Me\Desktop\CUO_Logs")
with open('2021_0638_118.json', 'r') as json_file:
	json_load = json.load(json_file)
	print(json_load)

data = json_load['fields']
for x in data:
	print(x['package_index'], x['timestamp'])