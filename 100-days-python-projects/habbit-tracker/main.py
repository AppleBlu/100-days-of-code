# Importing modules
import requests
import os
from datetime import datetime

# Retrieving today's date in the correct format
today_date = datetime.now().strftime("%Y%m%d")

USERNAME = "appleblu"
GRAPH_ID = "graph1"
PIXELA_USER_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_USER_ENDPOINT}/{USERNAME}/graphs"
PIXELA_GRAPH_ADD_ENDPOINT = f"{PIXELA_USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
PIXELA_GRAPH_EDIT_ENDPOINT = f"{PIXELA_USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"
TOKEN = os.environ.get("TOKEN")


# Params for the api calls
user_params = {
    # Like an api key (you make it your self)
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"

}
# Added header to the graph api call so my api key/token is invisible to hackers
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_add_config = {
    "date": today_date,
    "quantity": input(f"How many kilometers did you cycle today {USERNAME}? ")
}
graph_edit_config = {
    "quantity": "6.23"
}

# # Already made an account by running the code below. That's why its #
# # Sending data to the api
# response = requests.post(url=PIXELA_USER_ENDPOINT, json=user_params)
# # Checking if the call was successful
# print(response.text)

# Already made a graph by running the code below. That's why its #
# Sending data to the api to make a graph
# response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# Already made added a pixel to the graph by running the code below. That's why its #
# Sending data to the api to add a pixel
# response = requests.post(url=PIXELA_GRAPH_ADD_ENDPOINT, json=graph_add_config, headers=headers)
# print(response.text)

# Already edited a pixel on the graph by running the code below. That's why its #
# Sending data to the api to update a pixel to a different value using put
# response = requests.put(url=PIXELA_GRAPH_EDIT_ENDPOINT, json=graph_edit_config, headers=headers)
# print(response.text)

# Already deleted a pixel on the graph by running the code below. That's why its #
# Sending data to the api to delete a pixel on the graph
# response = requests.delete(url=PIXELA_GRAPH_EDIT_ENDPOINT, headers=headers)
# print(response.text)
