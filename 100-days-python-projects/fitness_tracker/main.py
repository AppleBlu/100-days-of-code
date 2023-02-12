# Importing modules
import os
import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 60
HEIGHT = 160.5
AGE = 21

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/491d1ee0411601d209b37ad274eff0b3/fitnessTracker/workouts"

# Asking the user what they did today
exercise_input = input("What exercise did you do today?: ")

# Getting today's date and time
today_date_and_time = datetime.now()
today_date = today_date_and_time.date().strftime("%d/%m/%Y")
time = today_date_and_time.strftime("%H:%M:%S")

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}
parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}


# Using Nutritionix to retrieve fitness data relevant to my exercise_input
response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
print(result)

exercise_duration = result["exercises"][0]["duration_min"]
exercise_name = result["exercises"][0]["name"]
exercise_calories = result["exercises"][0]["nf_calories"]

# Getting data to add to the api call when making a row on the spreadsheet
for exercise in result["exercises"]:
    sheety_params = {
        "workout": {
            "date": today_date,
            "time": time,
            "exercise": exercise_name.title(),
            "duration": exercise_duration,
            "calories": exercise_calories
        }
    }

    # Adding a row to my spreadsheet
    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params)
    response.raise_for_status()

# Retrieving the rows in my spreadsheet
response = requests.get(url=SHEETY_ENDPOINT)
response.raise_for_status()
row_result = response.json()
print(row_result)
