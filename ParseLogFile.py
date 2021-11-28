# Script created by Chiriac Adrian Stefan (adrian.chiriac@tremend.com)
# Brief : script to parse log file and determine if timestamps are correlated with the sample rates


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
frequency = {0.1: [9200, 10800],    # 8% max. deviation [ms]
             1: [920, 1080],        # 8% max. deviation [ms]
             10: [92, 108],         # 8% max. deviation [ms]
             20: [46, 54],          # 8% max. deviation [ms]
             100: [6, 14]           # 40% max. deviation [ms]
             }
timestamp_values_filtered_list = []

if int(package_type_ID) > 30 or int(package_type_ID) < 1:
    print("Package type ID must be between 1 and 30 according to the logging master scheme")
    exit()

frequency_by_sample_rate = [a for a, b in sample_rate.items() if int(package_type_ID) in b]
frequency_by_sample_rate = float(''.join(str(i) for i in frequency_by_sample_rate))
deviation_range = (frequency.get(float(f"{frequency_by_sample_rate}")))
min_frequency = deviation_range[0]
max_frequency = deviation_range[1]
print(f"Accepted frequency deviation range is between {min_frequency} and {max_frequency} milliseconds")

for file_name in sorted(os.listdir(folder_path)):
    print(f"Log file in process: {file_name}")
    os.chdir(folder_path)

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
            timestamp_values = int(''.join(signal_data_set))
            timestamp_values_filtered_list.append(timestamp_values)
            timestamp_values_filtered_list.sort(reverse=True)

    timestamp_difference = [x - y for x, y in zip(timestamp_values_filtered_list, timestamp_values_filtered_list[1:])]
    print(timestamp_difference)

    for value in timestamp_difference:
        if value not in range(min_frequency, max_frequency):
            raise AssertionError(f"Timestamps not correlated with the sample rate! Value {value} is out of range!")
        else:
            continue
