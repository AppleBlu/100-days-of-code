# Importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Keeping the browser in working state add options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)

# Pulling up the website below (amazon item for sale)
driver.get(url="https://www.amazon.co.uk")

# Accepting the cookies
# Finding the cookie button
cookie_button = driver.find_element(by="xpath", value='//*[@id="sp-cc-accept"]')

# Clicking the button
cookie_button.click()

# Navigating to the item we want the price for
# Finding the search bar
search = driver.find_element(by="xpath", value='//*[@id="twotabsearchtextbox"]')

# Typing in cow teddy into the search bar and clicking on the submit button
search.send_keys("cow teddy")
search.submit()


# Finding the item we want
item = driver.find_element(by="xpath", value='//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div'
                                             '/div/div/div[2]/div[1]/h2/a/span')

# Clicking on the item we want
item.click()

# Getting the price of the amazon item
price_pound = driver.find_element(by="class name", value="a-price-whole")
price_pence = driver.find_element(by="class name", value="a-price-fraction")

# Printing the price
print(f"£{price_pound.text}.{price_pence.text}")

# Getting the price_pence using another method (xpath)
# To do this I right-clicked on the element after inspecting and clicked copy > copy xpath
# I used single quotes because the xpath already had double quotes
price_pence_2 = driver.find_element(by="xpath",
                                    value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[3]')
print(price_pence_2.text)

# Closing the current tab
driver.close()

# Closes the entire browser
driver.quit()
