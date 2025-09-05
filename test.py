from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# set Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")   # open in full screen
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # avoid detection

# path to your chromedriver
service = Service("chromedriver.exe")  # or "./chromedriver" on Linux/Mac

# launch browser
driver = webdriver.Chrome(service=service, options=chrome_options)

# open a site
driver.get("https://google.com")

# search for something
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Hello Kiwi from ChatGPT!")
search_box.submit()
