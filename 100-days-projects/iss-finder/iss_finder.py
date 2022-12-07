import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 50.372812
MY_LONG = -4.145966
my_google_email = "codingtest1818@gmail.com"
password = 'mqodwegvlghwmwxb'


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if sunset < time_now.hour < sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and is_overhead():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_google_email, password=password)
            connection.sendmail(from_addr=my_google_email,
                                to_addrs="Blu18@protonmail.com",
                                msg="Subject:ISS\n\nLOOK UP!!!👆")
            connection.close()
