import smtplib
import random
import pandas
import os
import datetime as dt

MY_EMAIL = "testpython.g21@gmail.com"
PASSWORD = "cexjyj-3cawvu-vavseH"

birthdays = pandas.read_csv("birthdays.csv")
birthday_dict = birthdays.to_dict(orient="records")

now = dt.datetime.now()
day = now.day
current_month = now.month
for contact in birthday_dict:
    if day == contact['day'] and current_month == contact['month']:
        mail_chosen = random.choice(os.listdir("letter_templates/"))
        with open(f"letter_templates/{mail_chosen}") as email:
            mail_to_edit = email.read()
            mail_to_send = mail_to_edit.replace("[NAME]", contact['name'])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=contact['email'],
                                msg=f"Subject: Happy Birthday! \n\n {mail_to_send}")
