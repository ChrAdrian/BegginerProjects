# Script created by Chiriac Adrian Stefan (adrian.chiriac@tremend.com)
# Brief : script to transform .txt file into JSON file


import os
import re


signal_index = input("Please insert package index: ")
folder_path = r"C:\Users\Me\Desktop\CUO_Logs"

for file_name in sorted(os.listdir(folder_path)):
    print(f"Log file in process: {file_name}")
    os.chdir(folder_path)
    try:

        file_read = open(file_name, "r")

        lines = file_read.readlines()

        timestamp_list = []
        signal_index_list = []
        idx = 0

        for line in lines:

            if 'timestamp' in line:
                timestamp_list.insert(idx, line)
                idx += 1

            if 'index' in line:
                signal_index_list.insert(idx, line)

        file_read.close()

        if len(timestamp_list) == 0:
            print("\n\"" + "Timestamp" + "\" is not found in \"" + file_name + "\"!")
        else:
            timestamp_list = str([s.strip() for s in timestamp_list]).replace(",", "")
            timestamp_list = timestamp_list[2:-2].replace("'", "")
            timestamp_list = re.split(r"(\d+)", timestamp_list)

        if len(signal_index_list) == 0:
            print("\n\"" + "Signal index" + "\" is not found in \"" + file_name + "\"!")
        else:
            signal_index_list = str([s.strip() for s in signal_index_list]).replace(",", "")
            signal_index_list = signal_index_list[2:-2].replace("'", "")
            signal_index_list = re.split(r"(\d+)", signal_index_list)

        data = [j for i in zip(signal_index_list, timestamp_list) for j in i]
        data = data[:len(data) - 2]
        data = [data[n + 2:n + 4] for n in range(0, len(data), 4)]

        for sublist in data:
            if signal_index in sublist:
                sublist = [sublist[n + 1:n + 2] for n in range(0, len(sublist), 2)]
                signal_data_set = set([x for y in sublist for x in y])
                timestamp_values = ''.join(signal_data_set)
                print(timestamp_values)

    except:
        print("\nThe file doesn't exist!")
