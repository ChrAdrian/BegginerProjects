# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to log they keystrokes as a background application


from pynput.keyboard import Key, Listener


def key_press(key):
    print("{0} pressed".format(key))

def key_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()