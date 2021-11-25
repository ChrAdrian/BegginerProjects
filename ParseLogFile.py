# Script created by Chiriac Adrian Stefan (adrian.chiriac@tremend.com)
# Brief : script to parse CUO log file and determine if the timestamp si according to the frequency


import json
import os


folder_path = r"C:\Users\Me\Desktop\CUO_Logs"

for file_name in os.listdir(folder_path):
    os.chdir(folder_path)
    try:

        file_read = open(file_name, "r")

        lines = file_read.readlines()

        timestamp_list = []
        package_index_list = []
        idx = 0

        for line in lines:

            if 'timestamp' in line:
                timestamp_list.insert(idx, line)
                idx += 1

            if 'index' in line:
                package_index_list.insert(idx, line)

        file_read.close()

        if len(timestamp_list) == 0:
            print("\n\"" + "Timestamp" + "\" is not found in \"" + file_name + "\"!")
        else:
            timestamp_list = [s.strip() for s in timestamp_list]

        if len(package_index_list) == 0:
            print("\n\"" + "Package index" + "\" is not found in \"" + file_name + "\"!")
        else:
            package_index_list = [s.strip() for s in package_index_list]

    except:
        print("\nThe file doesn't exist!")