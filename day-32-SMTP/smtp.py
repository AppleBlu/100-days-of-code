import smtplib
import os

my_google_email = "codingtest1818@gmail.com"
password = os.environ.get("CODING_EMAIL_PASS")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_google_email, password=password)
    connection.sendmail(from_addr=my_google_email,
                        to_addrs="codingtest18@yahoo.com",
                        msg="Subject:Hello\n\nThis is the body of my email")
    connection.close()
