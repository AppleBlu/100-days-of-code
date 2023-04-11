# Importing modules
from flask import Flask, render_template
from datetime import datetime
import requests

# Setting the api url's required for the website
GENDER_API = "https://api.genderize.io?name="
AGE_API = "https://api.agify.io?name="

app = Flask(__name__)

# Getting the current date
current_date = datetime.now()
# Stripping the date to just get the time
current_year = str(current_date)[0: 4]


@app.route("/")
def home(name=None):
    # Adding a kwarg to to take in python code and insert it into the html file (template being rendered)
    return render_template("index.html", name=name, year=current_year)


@app.route("/<string:name>")
def guess_age_and_gender(name):
    response = requests.get(url=f"{GENDER_API}{name}")
    response.raise_for_status()
    gender_data = response.json()
    gender = gender_data["gender"]

    response = requests.get(url=f"{AGE_API}{name}")
    response.raise_for_status()
    age_data = response.json()
    age = age_data["age"]

    return render_template("name_calculator.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
