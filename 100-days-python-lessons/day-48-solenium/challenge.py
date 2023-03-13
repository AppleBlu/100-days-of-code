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

times = []
names = []

# Getting the times of the upcoming events
time_xpaths = ['//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time',
               '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time',
               '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]/time',
               '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]/time',
               '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]/time']


def get_times(xpath):
    time = driver.find_element(by="xpath", value=xpath)
    times.append(f"2023-{time.text}")


for path in time_xpaths:
    get_times(path)

# Getting the names of the upcoming events
name_xpaths = ['//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a',
               '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/a',
               '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]/a',
               '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]/a',
               '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]/a']


def get_names(xpath):
    name = driver.find_element(by="xpath", value=xpath)
    names.append(name.text)


for path in name_xpaths:
    get_names(path)

# Turning the lists into a dictionary
times_and_names = dict(zip(times, names))
print(times_and_names)

# Closing the website
driver.quit()
