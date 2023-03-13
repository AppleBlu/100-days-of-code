# Importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Keeping the browser in working state add options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)

# Pulling up the website below
driver.get(url="https://www.amazon.co.uk/Stuffed-Animal-Plush-Cuddly-Toddlers/dp/B09N1DZ6KQ/ref=sr_1_1_sspa?keywords=cow+teddy&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

# Closing the current tab
driver.close()

# Closes the entire browser
driver.quit()
