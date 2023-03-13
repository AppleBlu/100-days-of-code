# Importing modules
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

# Email details
my_google_email = "codingtest1818@gmail.com"
password = os.environ.get("CODING_EMAIL_PASS")
# Url of the product I want to buy
AMAZON_PRODUCT_URL = "https://www.amazon.co.uk/Apple-iPhone-14-256-GB/dp/B0BDJ9C67T/ref=sr_1_11?crid" \
                     "=23GR2YJLS7VO0&keywords=iphone+5c&qid=1677159945&sprefix=iphone+5c%2Caps%2C94&sr=8-11"

# Making a header for the request call
amazon_headers = {
    "Accept-Language": "en-GB,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 "
                  "Safari/537.36"
}

# Getting the html of the website in text format
response = requests.get(url=AMAZON_PRODUCT_URL, headers=amazon_headers)
response.raise_for_status()

# Converting the response text to html
soup = BeautifulSoup(response.text, "lxml")

# Getting the price of the product
price_tag = soup.find(name="span", class_="a-offscreen")
price_text = price_tag.getText()
# Removing the pound sign and turning the str into a float
price = float(price_text[1:])

# Getting the product name
product_tag = soup.find(name="span", class_="a-size-large product-title-word-break")
product_text = product_tag.getText()


# Checking to see if the price of the product is low enough for us to buy
if price < 800:
    # Sending my self an email with the details
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_google_email, password=password)
        connection.sendmail(from_addr=my_google_email,
                            to_addrs="codingtest18@yahoo.com",
                            msg=f"Subject:{product_text} has been reduced\n\n{product_text} is now only £{price}")
        connection.close()
