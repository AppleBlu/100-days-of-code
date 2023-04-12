# Importing modules
import requests


# Making a class to get data from an api
class Post:
    def __init__(self):
        # Setting the api for the blog post data
        self.api_url = "https://api.npoint.io/c790b4d5cab58020d391"
        # Calling the api url
        self.response = requests.get(url=self.api_url)
        # Checking the api call was successfully
        self.response.raise_for_status()
        # Using the data from the api call to turn it into a json file
        self.blog_data = self.response.json()
