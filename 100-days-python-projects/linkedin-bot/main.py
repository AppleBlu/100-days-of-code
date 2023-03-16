from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# Keeping the browser in working state add options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install())
                          , options=options)

# Pulling up the website below
driver.get(url="https://www.linkedin.com/?trk=public_jobs_nav-header-logo")

# Getting hold of the email input and password input
email = driver.find_element(by="xpath", value='//*[@id="session_key"]')
password = driver.find_element(by="xpath", value='//*[@id="session_password"]')

# Getting hold of the login button
login_button = driver.find_element(by="xpath", value='//*[@id="main-content"]/section[1]/div/div/form[1]'
                                                     '/div[2]/button')

# Auto login
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
login_button.click()

# Waiting for the website to load and then opening the job application section
time.sleep(5)
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3515188878&f_AL=true&f_E=2&geoId"
               "=102257491&keywords=python%20developer&location=London%2C%20England%2C%20"
               "United%20Kingdom")

# Finding the easy apply button
time.sleep(3)
easy_apply = driver.find_element(by="xpath", value='//*[@id="ember153"]')

# Clicking the easy apply button
easy_apply.click()

# Finding the phone number input
time.sleep(1)
phone_number_input = driver.find_element(by="xpath", value='//*[@id="single-line-text-form-component-'
                                                           'formElement-urn-li-jobs-applyformcommon-easyApply'
                                                           'FormElement-3515188878-9-phoneNumber-'
                                                           'nationalNumber"]')

# Inputting my random number
phone_number_input.send_keys("012345242")

# Last step would be to submit the application
# submit_button = driver.find_element(by="xpath", value='//*[@id="ember358"]/span')
# submit_button.click()
