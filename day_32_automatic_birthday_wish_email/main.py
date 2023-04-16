# import smtplib
# import datetime as dt
# import random
#
# email = 'hasna.akbarali98@gmail.com'
# password = 'gfksyaueznlsksju'
#
# def send_email():
#     # Start the connection in order to communicate with emails
#     with smtplib.SMTP("smtp.gmail.com",587) as connection:
#
#         # Transfer security protocol in case someone attempts to interrupt and reaed the email
#         connection.starttls()
#
#         connection.login(user=email,password=password)
#         connection.sendmail(from_addr=email,to_addrs='youngasu123@gmail.com',
#                             msg=f"Subject:Monday Motivation!\n\n{random.choice(data)}")
#
#
#
# today = dt.datetime.now().weekday()
# print(today)
#
# if today == 6:
#     with open('quotes.txt', 'r') as f:
#         data = f.readlines()
#     send_email()

import smtplib
import random
import datetime as dt
import pandas as pd

data = pd.read_csv('birthdays.csv')
today = dt.datetime.now()
from_email = 'hasna.akbarali98@gmail.com'
password = 'gfksyaueznlsksju'

month_day = (today.month, today.day)
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

def get_text():
    list_of_letters = ['letter1.txt', 'letter2.txt', 'letter3.txt']
    with open(random.choice(list_of_letters),'r') as f:
        file_data = f.readlines()
        file_data[0] = file_data[0].replace('[Name]', name)
    return ''.join(file_data)

if month_day in birthdays_dict:
    birthday_person = birthdays_dict[month_day]
    name = birthday_person['name']
    # print(name)
    to_email = birthday_person['email']
    # print(to_email)
    # get_text()
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr=from_email, to_addrs=to_email,
                            msg=f'Subject: Happy Birthday\n\n{get_text()}')
