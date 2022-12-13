# Importing modules
import requests
from twilio.rest import Client
import os

# Setting constants to the api info
API_KEY = os.environ.get("API_KEY")
ACCOUNT_SID_TWILIO = os.environ.get("ACCOUNT_SID_TWILIO")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
MY_NUMBER = os.environ.get("MY_NUMBER")
MY_LAT = 50.371394
MY_LONG = -4.142492

# Dict of parameters for the api call
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,alerts",
    "appid": API_KEY
}

# Retrieving data from the api
response = requests.get(OWM_ENDPOINT, params=weather_params)
# Checking for errors
response.raise_for_status()
# Converting the api data into a json file
weather_data = response.json()


def get_next_12_hours():
    """Collects id codes for the next 12 hours"""
    next_12_hours_list = []
    for index in range(12):
        next_12_hours = weather_data["hourly"][index]["weather"][0]["id"]
        next_12_hours_list.append(next_12_hours)
    return next_12_hours_list


# Quicker way of doing the above
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]

# Setting var to False
bring_umbrella = False

# If any of the codes are below 700 it will rain, and you will need an umbrella
for code in get_next_12_hours():
    if code < 700:
        # Setting var to True
        bring_umbrella = True

# If var is True print "Bring Umbrella"
if bring_umbrella:
    # Creating the client
    client = Client(ACCOUNT_SID_TWILIO, TWILIO_AUTH_TOKEN)
    # Sending the message
    message = client.messages.create(
        body="Bring an umbrella",
        from_="+14095097873",
        to=MY_NUMBER
    )
    # Checking status
    print(message.status)
