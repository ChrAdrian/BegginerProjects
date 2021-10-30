# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to do a countdown in seconds from 2 different dates given by the user


import datetime


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
# print(f"Current year: {current_year}, current month: {current_month}, current day: {current_day}, "
#       f"current hour: {current_hours}, current minute: {current_minutes}, current seccond: {current_seconds}")
# print(f"User year: {user_year}, user month: {user_month}, user day: {user_day}, "
#       f"user hour: {user_hours}, user minute: {user_minutes}, user seccond: {user_seconds}")