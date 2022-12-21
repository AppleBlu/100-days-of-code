# Importing modules
import requests
import os
USERNAME = "appleblu"
PIXELA_USER_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_USER_ENDPOINT}/{USERNAME}/graphs"
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
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}
# Added header to the graph api call so my api key/token is invisible to hackers
headers = {
    "X-USER-TOKEN": TOKEN
}


# Already made an account by running the code below. That's why its #
# Sending data to the api
# response = requests.post(url=PIXELA_USER_ENDPOINT, json=user_params)
# print(response.text)

# Already made a graph by running the code below. That's why its #
# Sending data to the api to make a graph
# response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

