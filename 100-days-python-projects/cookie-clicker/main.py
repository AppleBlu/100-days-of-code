# Importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# Keeping the browser in working state add options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)

# Pulling up the website below
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

# Finding the cookie
cookie = driver.find_element(by="css selector", value="#cookie")

# Finding the upgrades
items = driver.find_elements(by="css selector", value="#store div")
string_of_items = ""
for item in items:
    string_of_items += item.text

# Getting hold of all the item ids
item_ids = [item.get_attribute("id") for item in items]

# Finding the money
money = driver.find_element(by="xpath", value='//*[@id="money"]')

# Getting the time 5 seconds and 5 minutes from now
timeout = time.time() + 5  # 5seconds
five_min = time.time() + 60 * 5  # 5minutes


# Function for buying upgrades
def buy_upgrades():
    # Converting the money into an int
    money_number = money.text
    money_int = int(money_number.replace(",", ""))

    if 15 <= money_int < 100:
        driver.find_element(by="css selector", value=f"#{item_ids[0]}").click()
    elif 100 <= money_int < 500:
        driver.find_element(by="css selector", value=f"#{item_ids[1]}").click()
    elif 500 <= money_int < 2000:
        driver.find_element(by="css selector", value=f"#{item_ids[2]}").click()
    elif 2000 <= money_int < 7000:
        driver.find_element(by="css selector", value=f"#{item_ids[3]}").click()


while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:
        buy_upgrades()
        timeout = time.time() + 5  # 5seconds
    if time.time() > five_min:
        break
