import requests

API_KEY = "e817c21b4ae3a14803655ff2a55f5ecb"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
MY_LAT = 50.371394
MY_LONG = -4.142492

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
print(response.status_code)
print(response.json())
