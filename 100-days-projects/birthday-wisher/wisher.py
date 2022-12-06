import datetime as dt
import smtplib
import random
import pandas

current_date_time = dt.datetime.now()
current_month = current_date_time.month
current_day = current_date_time.day

birthday_person = None

GOOGLE_EMAIL = "codingtest1818@gmail.com"
PASSWORD = "mqodwegvlghwmwxb"

list_of_letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# 1. Update the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")

birthdays_dict = birthdays.to_dict()

days = birthdays['day'].tolist()
months = birthdays['month'].tolist()
names = birthdays['name'].tolist()
emails = birthdays['email'].tolist()
months_and_days = months + days
print(months_and_days)

print(months)
print(days)
print(names)
print(emails)

print(birthdays_dict)

for index in range(0, len(names)):
    if current_day == days[index] and current_month == months[index]:
        random_letter = random.choice(list_of_letters)
        with open(file=f"letter_templates/{random_letter}", mode="r") as letter:
            letter_contents = letter.read()
        with open(file=f"letter_templates/{random_letter}", mode="w") as letter:
            letter_with_name = letter_contents.replace("[NAME]", names[index])
            letter.write(letter_with_name)
        with open(file=f"letter_templates/{random_letter}", mode="r") as letter:
            finished_contents = letter.read()
            print(finished_contents)
#
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=GOOGLE_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=GOOGLE_EMAIL, to_addrs=emails[index],
                                msg=f"Subject: Happy Birthday {names[index]}!!!\n\n{finished_contents}")
            connection.close()
#

            reset_letter = letter_contents.replace("test", "[NAME]")
        with open(file=f"letter_templates/{random_letter}", mode="w") as letter:
            letter.write(reset_letter)
