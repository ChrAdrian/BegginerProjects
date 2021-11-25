# Script created by Chiriac Adrian Stefan (adrian.chiriac@tremend.com)
# Brief : script to parse CUO log file and determine if the timestamp si according to the frequency


import json
import os


folder_path = r"C:\Users\Me\Desktop\CUO_Logs"

for file_name in os.listdir(folder_path):
    os.chdir(folder_path)
    try:

        # opening and reading the file
        file_read = open(file_name, "r")

        # reading file content line by line.
        lines = file_read.readlines()

        timestamp_list = []
        idx = 0

        # looping through each line in the file
        for line in lines:

            # if line have the input string, get the index
            # of that line and put the
            # line into newly created list
            if 'timestamp' in line:
                timestamp_list.insert(idx, line)
                idx += 1

        # closing file after reading
        file_read.close()

        # if length of new list is 0 that means
        # the input string doesn't
        # found in the text file
        if len(timestamp_list) == 0:
            print("\n\"" + "Timestamp" + "\" is not found in \"" + file_name + "\"!")
        else:

            # displaying the lines
            # containing given string
            lineLen = len(timestamp_list)
            print("\n**** Lines containing \"" + "timestamp" + "\" ****\n")
            for i in range(lineLen):
                print(end=timestamp_list[i])
            print()

    # entering except block
    # if input file doesn't exist
    except:
        print("\nThe file doesn't exist!")