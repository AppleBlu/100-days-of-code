# Importing modules
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Constants
TWITTER_EMAIL = os.environ.get("EMAIL")
TWITTER_PASSWORD = os.environ.get("PASSWORD")
TWITTER_USERNAME = os.environ.get("USERNAME")
PROMISED_DOWN = 150
PROMISED_UP = 10

# Keeping the browser in working state add options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install())
                          , options=options)

# Pulling up the website below
driver.get(url="https://www.speedtest.net/")

# Waiting for page to load
time.sleep(1)

# Finding the cookie accept button and clicking on it
cookie_button = driver.find_element(by="xpath", value='//*[@id="onetrust-accept-btn-handler"]')
cookie_button.click()

# Finding and clicking the test internet speed button (GO) and clicking it
go = driver.find_element(by="xpath", value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
go.click()

# Waiting to test internet connection
time.sleep(45)

# Finding the download and upload speed results
download = driver.find_element(by="xpath", value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                 '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')

upload = driver.find_element(by="xpath", value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div'
                                               '[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
download_number = download.text
upload_number = upload.text

# Opening twitter
driver.get(url="https://twitter.com/?lang=en")

# Waiting for page to load
time.sleep(1)

# Finding and clicking login
login = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a')
login.click()

# Waiting for page to load
time.sleep(2)

# Finding and entering the email
email_entry = driver.find_element(by="xpath", value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div'
                                                    '[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]'
                                                    '/div/input')
email_entry.send_keys(TWITTER_EMAIL)

# Finding the next button and clicking it
next_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div'
                                                    '[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
next_button.click()

# Waiting for page to load
time.sleep(1)

# Finding the username entry and entering the username
username_entry = driver.find_element(by="xpath", value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                       '/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div'
                                                       '[2]/div/input')
username_entry.send_keys(TWITTER_USERNAME)

# Finding and pressing the next button
next_button_2 = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/'
                                                                 'div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div'
                                                                 '/div/div/div')
next_button_2.click()

# Waiting for page to load
time.sleep(1)

# Finding the password entry and entering my password
password_entry = driver.find_element(by="xpath", value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                       '/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/'
                                                       'div/div[2]/div[1]/input')
password_entry.send_keys(TWITTER_PASSWORD)

# Finding and pressing the login button after entering my credentials
login_button_after_creds = driver.find_element(by="xpath", value='//*[@id="layers"]/div[2]/div/div/div/div/'
                                                                 'div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/'
                                                                 'div[1]/div/div/div')
login_button_after_creds.click()

# Waiting for page to load
time.sleep(3)

# Finding the tweet button and clicking it
tweet_button = driver.find_element(by="xpath", value='//*[@id="react-root"]/div/div/div[2]/header/div/div'
                                                     '/div/div[1]/div[3]/a')
tweet_button.click()

# Waiting for page to load
time.sleep(2)

# Entering my message
message_field = driver.find_element(by="xpath", value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div'
                                                      '[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div'
                                                      '[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/'
                                                      'div/div/div/div/div[2]/div/div/div/div')
message_field.send_keys(f"I am getting a download speed of: {download_number} and an upload speed of: "
                        f"{upload_number} at sky")

# Finding and clicking the send button for my message
send_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div'
                                                    '[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div'
                                                    '[3]/div/div/div[2]/div[4]')
send_button.click()
