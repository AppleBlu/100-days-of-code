# Importing modules
import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client

# Setting constants
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("M_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCK_ENDPOINT = "http://api.marketstack.com/v1/eod"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
MY_NUMBER = os.environ.get("MY_NUMBER")
ACCOUNT_SID_TWILIO = os.environ.get("T_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("T_AUTH_TOKEN")

# Getting yesterday's date and two days ago date
one_day_ago = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
two_days_ago = (datetime.now() - timedelta(2)).strftime("%Y-%m-%d")

# Setting params for the api calls
stock_params = {
    'access_key': STOCK_API_KEY,
    'symbols': STOCK_NAME,
    'date_from': two_days_ago,
    'date_to': one_day_ago
}
news_params = {
    "q": "Tesla",
    "from": two_days_ago,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}

# Retrieving data from the api
stock_api_results = requests.get(url=STOCK_ENDPOINT, params=stock_params)
# Checking for error codes
stock_api_results.raise_for_status()
# Getting a json file with the results of the api
stock_api_response = stock_api_results.json()

# Getting yesterday's and two days ago closing stock values
yesterday_closing = stock_api_response["data"][0]["close"]
two_days_ago_closing = stock_api_response["data"][0]["open"]

# Finding the positive difference between the two values
difference = abs(float(yesterday_closing) - float(two_days_ago_closing))

# Working out the percentage of the difference
difference_percent = (difference / float(yesterday_closing)) * 100

# Retrieving data from the api
news_api_results = requests.get(url=NEWS_ENDPOINT, params=news_params)
# Checking for error codes
news_api_results.raise_for_status()
# Getting a json file with the results of the api
news_api_response = news_api_results.json()
# Getting the first 3 articles
three_news_articles = news_api_response["articles"][0:3]
# Getting the first three article titles
title_one = three_news_articles[0]["title"]
title_two = three_news_articles[1]["title"]
title_three = three_news_articles[2]["title"]
# Getting the first three article descriptions
description_one = three_news_articles[0]["url"]
description_two = three_news_articles[1]["url"]
description_three = three_news_articles[2]["url"]

# Checking to see the percent diff is more than 5
if difference_percent > 5:
    # Creating the client
    client = Client(ACCOUNT_SID_TWILIO, TWILIO_AUTH_TOKEN)
    # Sending the message
    message = client.messages.create(
        body=f"\nTSLA 🔺{int(difference_percent)}%\n{title_one}\n{description_one}\n\nTSLA 🔺{int(difference_percent)}%\n"
             f"{title_two}\n{description_two}\n\nTSLA 🔺{int(difference_percent)}%{title_three}\n"
             f"{description_three}",
        from_="+14095097873",
        to=MY_NUMBER
    )
    # Checking status
    print(message.status)
