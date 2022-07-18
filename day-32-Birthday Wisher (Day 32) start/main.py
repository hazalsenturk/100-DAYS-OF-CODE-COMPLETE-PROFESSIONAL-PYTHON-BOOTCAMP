# import smtplib
#
# my_email = "testpython.y21@yahoo.com"
# password = "njwhvoiwkjdqkyxh"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()  #makes the connection secure
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="testpython.g21@gmail.com",
#                         msg="Subject:Hello\n\nfrom yahoo to gmail")

import smtplib
import datetime as dt
import random

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1993, month=8, day=24,hour=4)
# print(date_of_birth)

my_email = "testpython.g21@gmail.com"
password = "cexjyj-3cawvu-vavseH"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 3:

    with open("quotes.txt") as data:
        quote_list = data.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="testpython.y21@yahoo.com",
                            msg=f"Subject:Boost-up\n\n {random.choice(quote_list)}")
