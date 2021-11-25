# Script created by Chiriac Adrian Stefan (adrian.chiriac@tremend.com)
# Brief : script to parse JSON file


import json
import os


os.chdir(r"C:\Users\Me\Desktop\CUO_Logs")
with open('test1.json', 'r') as json_file:
	json_load = json.load(json_file)
	print(json_load)