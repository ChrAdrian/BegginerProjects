# Script created by Chiriac Adrian Stefan (adrian.chiriac@tremend.com)
# Brief : script to transform .txt file into JSON file


import json
import os
import re


package_index = input("Please insert package index: ")
folder_path = r"C:\Users\Me\Desktop\CUO_Logs"

for file_name in sorted(os.listdir(folder_path)):
    print(f"Log file in process: {file_name}")
    os.chdir(folder_path)
    # try:

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
        timestamp_list = str([s.strip() for s in timestamp_list]).replace(",", "")
        timestamp_list = timestamp_list[2:-2].replace("'", "")
        timestamp_list = re.split(r"(\d+)", timestamp_list)

    if len(package_index_list) == 0:
        print("\n\"" + "Package index" + "\" is not found in \"" + file_name + "\"!")
    else:
        package_index_list = str([s.strip() for s in package_index_list]).replace(",", "")
        package_index_list = package_index_list[2:-2].replace("'", "")
        package_index_list = re.split(r"(\d+)", package_index_list)

    data = [j for i in zip(package_index_list, timestamp_list) for j in i]
    data = data[:len(data) - 2]
    data = [data[n + 2:n + 4] for n in range(0, len(data), 4)]
    for sublist in data:
        if package_index in sublist:
            sublist = [sublist[n + 1:n + 2] for n in range(0, len(sublist), 2)]
            data_set = set([x for y in sublist for x in y])
            timestamp_values = ''.join(data_set)
            print(timestamp_values)

    # except:
    #     print("\nThe file doesn't exist!")
