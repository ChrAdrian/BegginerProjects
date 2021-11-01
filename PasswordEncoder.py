# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to generate a random password from a given string, store it and if needed decoded to the initial string


import random
import string
import re

#user_string = input('Enter password: ')


def generate_password(user_string):
    # Generate a random string that matches the lenght of the user password
    lenght = len(user_string)
    comp_string = string.ascii_letters + string.digits + string.punctuation
    rand_string = ''.join(random.choice(comp_string) for i in range(lenght))
    # print(rand_string)
    # Generate a new string by merging the user password and the random string
    new_string = ""
    for letter in range(lenght):
        new_string += user_string[letter]
        new_string += rand_string[letter]
    new_string = new_string[::-1]
    # print(new_string)
    return new_string, rand_string


def write_password_to_file(new_string, rand_string):
    # Open text file
    text_file = open(r"C:\Users\Me\Desktop\Passwords.txt", "w")
    # Write string to file
    text_file.write(f'Password is: {new_string} with the following encoding: {rand_string}')
    # Close file
    text_file.close()

def decode_password():
    path = input('Enter path to password file: ')
    # Read the entire file to a string
    with open(path, 'rt') as myfile:
        contents = myfile.read()
    # Isolate the encoded password
    start1 = 'is: '
    end1 = ' with'
    r1 = re.findall(re.escape(start1) + "(.+?)" + re.escape(end1), contents)
    # Convert to string the list elements
    string_contents_1 = ''.join(str(element_1) for element_1 in r1)
    # Rebuild the initial user password
    recovered_new_string = re.sub("[|]", '', string_contents_1)[::-1][::2]
    print(recovered_new_string)


# new_string, rand_string = generate_password(user_string)
# write_password_to_file(new_string, rand_string)
# decode_password()