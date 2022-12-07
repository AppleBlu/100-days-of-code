# Importing modules
import datetime as dt
import smtplib
import random
import pandas

# Getting hold the current date and time
current_date_time = dt.datetime.now()
current_month = current_date_time.month
current_day = current_date_time.day

# Getting hold of the email login for the email iam going to be sending from
GOOGLE_EMAIL = "codingtest1818@gmail.com"
PASSWORD = "mqodwegvlghwmwxb"

list_of_letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# Reading the birthdays.csv with pandas
birthdays = pandas.read_csv("birthdays.csv")

# Getting hold of all the separate information from the csv file
days = birthdays['day'].tolist()
months = birthdays['month'].tolist()
names = birthdays['name'].tolist()
emails = birthdays['email'].tolist()

# for loop to check if the current date and time matches with anyone's birthdate
for index in range(0, len(names)):
    if current_day == days[index] and current_month == months[index]:

        # Retrieving a random letter
        random_letter = random.choice(list_of_letters)

        # ----File manipulation------
        # Retrieving the contents of the random letter
        with open(file=f"letter_templates/{random_letter}", mode="r") as letter:
            letter_contents = letter.read()
        # Replacing the [NAME] with the name of the birthday person
        with open(file=f"letter_templates/{random_letter}", mode="w") as letter:
            letter_with_name = letter_contents.replace("[NAME]", names[index])
            letter.write(letter_with_name)
        # Finally reading the letter again
        with open(file=f"letter_templates/{random_letter}", mode="r") as letter:
            finished_contents = letter.read()
            print(finished_contents)

        # Sending the happy birthday letter to the correct email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=GOOGLE_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=GOOGLE_EMAIL, to_addrs=emails[index],
                                msg=f"Subject: Happy Birthday {names[index]}!!!\n\n{finished_contents}")
            connection.close()

            # Resetting the person name with [NAME] again
            reset_letter = letter_contents.replace("test", "[NAME]")
        with open(file=f"letter_templates/{random_letter}", mode="w") as letter:
            letter.write(reset_letter)
