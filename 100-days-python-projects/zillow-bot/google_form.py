from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import random

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
CHROME_DRIVER_PATH = 'C:/Users/A12/PycharmProjects/chromedriver.exe'


class GoogleForm:
    def __init__(self):
        self.google_form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfHMn1-5rg6AiefsQfA5C3IPV9bEE7cs' \
                               'UKpA6Dz6EV4Sr-NBw/viewform?usp=sf_link'
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)

    def update_form(self, a_list, p_list, l_list):
        driver = self.driver
        driver.maximize_window()

        for i in range(len(l_list)):
            driver.get(self.google_form_url)
            sleep(1)
            first_answer = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
                                                         '2]/div/div[1]/div/div[1]/input')
            first_answer.send_keys(a_list[i])

            second_answer = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div['
                                                          '2]/div/div[1]/div/div[1]/input')
            second_answer.send_keys(p_list[i])

            third_answer = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div['
                                                         '2]/div/div[1]/div/div[1]/input')
            third_answer.send_keys(l_list[i])

            submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div['
                                                          '1]/div/span/span')
            submit_button.click()
            sleep_list = [0.1, 0.12, 0.15, 0.13]
            sleep(random.choice(sleep_list))
