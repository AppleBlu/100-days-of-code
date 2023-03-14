# Importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Keeping the browser in working state add options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)

# Pulling up the website below
driver.get(url="https://www.python.org")

# Getting the times and names of the events in a selenium object
event_times = driver.find_elements(by="css selector", value=".event-widget time")
event_names = driver.find_elements(by="css selector", value=".event-widget ul a")

# Making a dictionary with names and times
events = {}
for n in range(0, len(event_times)):
    events[n] = {"time": event_times[n].text, "name": event_names[n].text}

# Printing the dictionary
print(events)

# Closing the website
driver.quit()
