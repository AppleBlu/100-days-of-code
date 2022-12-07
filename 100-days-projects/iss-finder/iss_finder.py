import requests
from datetime import datetime

MY_LAT = 50.372812
MY_LONG = -4.145966

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunset)

time_now = datetime.now()
print(time_now)
