# Importing modules
import requests
import os

# Getting hidden endpoint from environment variable
SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")


class DataManager:
    """Handles data using an api"""

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Gets data from the Google sheet"""
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        # Sets self.destination_data equal to the data retrieved from the api
        self.destination_data = data["prices"]
        # Returns the data
        return self.destination_data

    def update_destination_codes(self):
        """Updates the Google sheet with correct values for iata codes"""
        # For each city on the Google sheet
        for city in self.destination_data:
            # Params for the sheety api
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            # Updating the iataCode row on the Google sheet with the correct values using an api put() call
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            # (check-test) Printing the updated json file in a text format to the terminal
            print(response.text)
