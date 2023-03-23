# Importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os


# Making a class for our instagram bot
class InstaFollower:
    def __init__(self):
        # Using environment variables to hide sensitive information
        self.EMAIL = os.environ.get("EMAIL")
        self.PASSWORD = os.environ.get("PASSWORD")
        # Keeping the browser in working state and adding options
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()),
                                       options=self.options)

    def login(self):
        """Brings up the instagram website and logs in automatically"""
        self.driver.get(url="https://instagram.com/")
        # Waiting for the page to load and allowing the user to click the cookie accept button
        time.sleep(5)

        # Finding the email and password entry's and entering them
        email_entry = self.driver.find_element(by="xpath", value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_entry = self.driver.find_element(by="xpath", value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        email_entry.send_keys(self.EMAIL)
        password_entry.send_keys(self.PASSWORD)

        # Finding the login button and clicking it
        self.driver.find_element(by="xpath", value='//*[@id="loginForm"]/div/div[3]/button/div').click()
        # Waiting to load the page
        time.sleep(5)

    def find_followers(self):
        """Once logged in this function will find an instagram account and bring up all the followers of that account"""
        # Finding the instagram account we want
        self.driver.get("https://www.instagram.com/chefsteps/")

        # Waiting
        time.sleep(2)
        # Finding and clicking the followers button
        self.driver.find_element(by="xpath", value='//*[@id="react-root"]/section/main/div/header/section'
                                                   '/ul/li[2]/a').click()
        # Waiting
        time.sleep(2)
        # Finding the popup and scrolling down
        modal = self.driver.find_element(by="xpath", value='/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        """Will follow every account that it finds"""
        # Finding all the follow buttons
        all_buttons = self.driver.find_elements(by="css selector", value="li button")

        # For loop to click follow every second
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)

            # If exception find and click the cancel button
            except ElementClickInterceptedException:
                self.driver.find_element(by="xpath", value='/html/body/div[5]/div/div/div/div[3]/button[2]').click()


# Initialising InstaFollower class and calling the necessary functions
my_insta_bot = InstaFollower()
my_insta_bot.login()
my_insta_bot.find_followers()
