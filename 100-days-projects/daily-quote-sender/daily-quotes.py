import random
import datetime as dt
import smtplib

current_date_time = dt.datetime.now()
day_of_week = current_date_time.weekday()

with open(file="quotes.txt") as data:
    quotes = data.readlines()

GOOGLE_EMAIL = "codingtest1818@gmail.com"
PASSWORD = "mqodwegvlghwmwxb"

random_quote = random.choice(quotes)

if day_of_week == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=GOOGLE_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=GOOGLE_EMAIL, to_addrs="blu18@protonmail.com",
                            msg=f"Subject: Daily quote\n\n{random_quote}")
        connection.close()
