# Importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Using environment variables to hide sensitive information
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# Keeping the browser in working state add options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)

# Pulling up the website below
driver.get(url="https://tinder.com/")
# Getting hold og the base window (the first one)
base_window = driver.window_handles[0]

# Waiting for the page to load
time.sleep(2)

# Getting hold of the login button and clicking it
login_button = driver.find_element(by="xpath", value='//*[@id="q-586956664"]/div/div[1]/div/main/div[1]'
                                                     '/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

# Waiting for the page to load
time.sleep(2)

# Getting hold of the facebook login button and clicking it
facebook_login = driver.find_element(by="xpath", value='//*[@id="q1979629556"]/main/div/div/div[1]/div/div'
                                                       '/div[3]/span/div[2]/button/div[2]/div[2]/div/div')
facebook_login.click()

# Waiting for the pop-up to load
time.sleep(3)

# Switching over to the new pop-up window
facebook_login_window = driver.window_handles[1]
driver.switch_to.window(facebook_login_window)

# Getting facebook credential inputs and inputting the required credentials
email = driver.find_element(by="xpath", value='//*[@id="email"]')
password = driver.find_element(by="xpath", value='//*[@id="pass"]')
email.send_keys(EMAIL)
password.send_keys(PASSWORD)

# Getting hold of the login button and clicking it
time.sleep(1)
facebook_login_2 = driver.find_element(by="name", value='login')
facebook_login_2.click()

# Waiting for page to load
time.sleep(8)

# Switching over to the new pop-up window
tinder_window = driver.window_handles[0]
driver.switch_to.window(tinder_window)

# Finding the location permission button and clicking it
location_permission = driver.find_element(by="xpath", value='//*[@id="q1979629556"]/main/div/div/div/div[3]/'
                                                            'button[1]/div[2]/div[2]')
location_permission.click()

# Finding the notification permission button and clicking it
time.sleep(1)
notification_permission = driver.find_element(by="xpath", value='//*[@id="q1979629556"]/main/div/div/div'
                                                                '/div[3]/button[2]/div[2]/div[2]')
notification_permission.click()

# Finding the swipe left button and clicking it
time.sleep(3)
swipe_left = driver.find_element(by="xpath", value='//*[@id="q-586956664"]/div/div[1]/div/main/div[1]'
                                                   '/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button/span/span')

# Swiping left every 1 second
while True:
    time.sleep(1)
    swipe_left.click()
