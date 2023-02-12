# Importing modules
import requests

# Setting parameters for the API call
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

# Retrieving the results from the api and getting hold of the question
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
