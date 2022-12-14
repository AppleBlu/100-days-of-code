import random
import smtplib
import os

with open(file="quotes.txt") as data:
    quotes = data.readlines()

GOOGLE_EMAIL = "codingtest1818@gmail.com"
PASSWORD = os.environ.get("CODING_EMAIL_PASS")

random_quote = random.choice(quotes)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=GOOGLE_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=GOOGLE_EMAIL, to_addrs="blu18@protonmail.com",
                        msg=f"Subject: Daily quote\n\n{random_quote}")
    connection.close()
