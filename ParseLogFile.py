# Script created by Chiriac Adrian Stefan (adrian.chiriac@tremend.com)
# Brief : script to transform .txt file into JSON file


import os
import re

package_type_ID = input("Please insert package index: ")
folder_path = r"C:\Users\Me\Desktop\CUO_Logs"
sample_rate = {0.1: [10, 11],
               1: [9, 12, 24, 25],
               10: [1, 4, 17, 28, 29],
               20: [2, 5, 6, 7, 8, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 26, 27, 30],
               100: [3]
               }
frequency = {0.1: 10000,
             1: 1000,
             10: 100,
             20: 50,
             100: 10
             }
timestamp_values_filtered_list = []

if int(package_type_ID) > 30 or int(package_type_ID) < 1:
    print("Package type ID must be between 1 and 30 according to the logging master scheme")
    exit()

for file_name in sorted(os.listdir(folder_path)):
    print(f"Log file in process: {file_name}")
    os.chdir(folder_path)
    try:

        file_read = open(file_name, "r")

        lines = file_read.readlines()

        timestamp_list = []
        package_type_ID_list = []
        idx = 0

        for line in lines:

            if 'timestamp' in line:
                timestamp_list.insert(idx, line)
                idx += 1

            if 'index' in line:
                package_type_ID_list.insert(idx, line)

        file_read.close()

        if len(timestamp_list) == 0:
            print("\n\"" + "Timestamp" + "\" is not found in \"" + file_name + "\"!")
        else:
            timestamp_list = str([s.strip() for s in timestamp_list]).replace(",", "")
            timestamp_list = timestamp_list[2:-2].replace("'", "")
            timestamp_list = re.split(r"(\d+)", timestamp_list)

        if len(package_type_ID_list) == 0:
            print("\n\"" + "Signal index" + "\" is not found in \"" + file_name + "\"!")
        else:
            package_type_ID_list = str([s.strip() for s in package_type_ID_list]).replace(",", "")
            package_type_ID_list = package_type_ID_list[2:-2].replace("'", "")
            package_type_ID_list = re.split(r"(\d+)", package_type_ID_list)

        data = [j for i in zip(package_type_ID_list, timestamp_list) for j in i]
        data = data[:len(data) - 2]
        data = [data[n + 2:n + 4] for n in range(0, len(data), 4)]

        for sublist in data:
            if package_type_ID in sublist:
                sublist = [sublist[n + 1:n + 2] for n in range(0, len(sublist), 2)]
                signal_data_set = set([x for y in sublist for x in y])
                timestamp_values = ''.join(signal_data_set)
                timestamp_values_filtered_list.append(timestamp_values)
        print(timestamp_values_filtered_list)

    except:
        print("\nThe file doesn't exist!")
