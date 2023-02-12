import requests

"""Status codes (X can be any number)
Wait something is happening: 1XX
Success you got the data you wanted: 2XX
You cant get hold of this data: 3XX
You failed or the data does not exist: 4XX
The server or something not controlled by you has failed: 5XX"""

"""Api commands
get() - get the data from the api
post() - add data to the api
put() - update the data in the api
delete() - delete date from the api"""

# Trying to receive data from this api
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

# Checking if we can get the data (You would add more but this is just an example)
if response.status_code == 404:
    raise Exception("That response does not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorised to access this data.")

# Quicker way of doing this using the request module
# Will raise the appropriate error for you
response.raise_for_status()

# Receiving the actual date we want
data = response.json()
print(data)

# Getting a specific key
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# Turning are data into a tuple
iss_position = (longitude, latitude)
print(iss_position)

