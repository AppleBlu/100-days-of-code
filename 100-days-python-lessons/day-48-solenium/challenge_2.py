# Importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Keeping the browser in working state add options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)

# Getting hold of the website we need to scrape
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Getting hold of the data we need
article_count_data = driver.find_element(by="css selector", value="#articlecount a")

# Printing the data
print(article_count_data.text)

# Closing the website
driver.quit()
