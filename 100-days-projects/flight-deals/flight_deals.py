# Importing modules
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

# Creating objects from classes
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Getting the Google sheet data
sheet_data = data_manager.get_destination_data()

# Checking if a row is empty
if sheet_data[0]["iataCode"] == "":
    # For each row on the Google sheet
    for row in sheet_data:
        # Collecting iata codes from an api
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    # Updating the json file with correct values
    data_manager.destination_data = sheet_data
    # Using an api call to update the Google sheet with the new json file
    data_manager.update_destination_codes()

# Getting tomorrows datetime
tomorrow = datetime.now() + timedelta(days=1)
# Getting 6months from now datetime
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# For each iata code find flights between these times
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    # If the flight price is lower than the lowest price stated on the Google sheet
    if flight.price < destination["lowestPrice"]:

        # Send a sms message to alert the user
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to"
                    f" {flight.destination_city}-{flight.destination_airport}, from {flight.out_date}"
                    f" to {flight.return_date}."
        )
