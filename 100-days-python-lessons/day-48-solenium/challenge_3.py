# Importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Keeping the browser in working state add options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)

# Pulling up the website below
driver.get(url="https://web.archive.org/web/20190201181142/http://secure-retreat-92358.herokuapp.com:80/")

# Finding the three form entries
first_name = driver.find_element(by="xpath", value='/html/body/form/input[1]')
last_name = driver.find_element(by="xpath", value='/html/body/form/input[2]')
email = driver.find_element(by="xpath", value='/html/body/form/input[3]')

# Finding the submit button
submit_button = driver.find_element(by="class name", value="btn-primary")

# Entering details into the entries
first_name.send_keys("Random")
last_name.send_keys("Name")
email.send_keys("RandomEmail@random.com")

# Clicking the submit button
submit_button.click()

# Closing the website
# driver.quit()
