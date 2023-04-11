# Importing modules
from flask import Flask, render_template
from datetime import datetime
import requests

# Setting the api url's required for the website
GENDER_API = "https://api.genderize.io?name="
AGE_API = "https://api.agify.io?name="

# Creating the flask app
app = Flask(__name__)

# Getting the current date
current_date = datetime.now()
# Stripping the date to just get the time
current_year = str(current_date)[0: 4]


# When on the home route of the website run this function
@app.route("/")
def home(name=None):
    # Adding a kwarg to take in python code and insert it into the html file (template being rendered)
    return render_template("index.html", name=name, year=current_year)


# When on the /name route of the website run this function
@app.route("/<string:name>")
# Function takes in the name (string) that is typed into the url after the /
def guess_age_and_gender(name):
    # Using the gender api with the name passed into the url
    response = requests.get(url=f"{GENDER_API}{name}")
    # Checking for any errors involving the api call
    response.raise_for_status()
    # Collecting the data in a json format from the api call
    gender_data = response.json()
    # Selecting the specific piece of data that we require
    gender = gender_data["gender"]

    # Repeating the process for the age api
    response = requests.get(url=f"{AGE_API}{name}")
    response.raise_for_status()
    age_data = response.json()
    age = age_data["age"]

    # Rendering the template and passing in data
    return render_template("name_calculator.html", name=name, gender=gender, age=age)


# If name is the same as __main__ then run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
