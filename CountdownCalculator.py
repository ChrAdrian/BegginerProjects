# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to do a countdown in seconds from current date and date given by the user


import datetime
import time


global user_date

# Countdown function
def countdown(diff):
    global user_date
    while diff > 0:
        diff -= 1
        time.sleep(1)
        print(f"\r{diff} seconds remaining until {user_date}.", end='')

def main():
    global user_date
    # Get inputs from user, define errors and sepparate each time variable
    get_current_time = datetime.datetime.now()
    current_system_time = get_current_time.strftime("%Y-%m-%d %H:%M:%S")
    current_time = current_system_time.split(' ')[1]
    current_hours = current_time.split(':')[0]
    current_minutes = current_time.split(':')[1]
    current_seconds = current_time.split(':')[2]
    current_date = current_system_time.split(' ')[0]
    current_year = current_date.split('-')[0]
    current_month = current_date.split('-')[1]
    current_day = current_date.split('-')[2]
    user_date_time = input ("Insert date in the following format YYYY-MM-DD HH:MM:SS: ")
    user_date = user_date_time.split(' ')[0]
    if "/" in user_date:
        user_date = user_date.replace('/', '-')
    user_year = user_date.split('-')[0]
    user_month = user_date.split('-')[1]
    user_day = user_date.split('-')[2]
    if int(user_month) > 12 or int(user_day) > 31:
        print("Wrong date format!")
    if len(user_year) < 4 or len(user_month) > 2 or len(user_day) > 2:
        print("Wrong date format!")
        exit()
    user_time = user_date_time.split(' ')[1]
    if ":" not in user_time:
        print("Please add ':' in the time format!")
        exit()
    user_hours = user_time.split(':')[0]
    user_minutes = user_time.split(':')[1]
    user_seconds = user_time.split(':')[2]
    if int(user_hours) > 24 or int(user_minutes) > 60 or int(user_seconds) > 60:
        print("Wrong time format, please use 24h format!")
        exit()
    if len(user_hours) != 2 or len(user_minutes) != 2 or len(user_seconds) != 2:
        print("Wrong time format, please use 2 digits format!")
        exit()
    # Transform dates to strings
    user_date = datetime.datetime(int(user_year), int(user_month), int(user_day), hour=int(user_hours),
                minute=int(user_minutes), second=int(user_seconds))
    current_date = datetime.datetime(int(current_year), int(current_month), int(current_day), hour=int(current_hours),
                minute=int(current_minutes), second=int(current_seconds))
    user_date_filtered = ''.join(filter(str.isalnum, str(user_date)))
    current_date_filtered = ''.join(filter(str.isalnum, str(current_date)))
    # Define past or future date differences
    if int(current_date_filtered) < int(user_date_filtered):
        difference = user_date - current_date
        difference_in_seconds = difference.total_seconds()
        return difference_in_seconds
    else:
        difference = current_date - user_date
        difference_in_seconds = difference.total_seconds()
        while difference_in_seconds > 0:
            difference_in_seconds += 1
            time.sleep(1)
            print(f"\r{difference_in_seconds} seconds have passed since {user_date}.", end='')


countdown(main())

