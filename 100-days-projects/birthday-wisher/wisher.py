import datetime as dt
import smtplib
import random
import pandas

current_date_time = dt.datetime.now()
current_month = current_date_time.month
current_day = current_date_time.day

GOOGLE_EMAIL = "codingtest1818@gmail.com"
PASSWORD = "mqodwegvlghwmwxb"

list_of_letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

random_letter = random.choice(list_of_letters)

# 1. Update the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")
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

# 2. Check if today matches a birthday in the birthdays.csv
for index in range(0, len(names)):
    if current_day == days[index] and current_month == months[index]:
        persons_birthday = names[index]
        with open(file=f"letter_templates/{random_letter}", mode="r") as letter:
            letter_contents = letter.read()
            letter_with_name = letter_contents.replace("[NAME]", persons_birthday)
            letter_with_both_names = letter_with_name.replace("Angela", "Tom")
        with open(file=f"letter_templates/{random_letter}", mode="w") as letter:
            letter.write(letter_with_both_names)
        with open(file=f"letter_templates/{random_letter}", mode="r") as letter:
            finished_letter = letter.read()

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=GOOGLE_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=GOOGLE_EMAIL, to_addrs="14kennys@gmail.com",
                                msg=f"Subject: Happy Birthday!!!\n\n{finished_letter}")
            connection.close()
