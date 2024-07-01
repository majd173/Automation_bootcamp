
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# infra
driver = webdriver.Chrome()  # Chrome() is a constructor that initializes (opens) a chrome web-browser

# infra    # logic
driver.get('https://www.youtube.com/')

# logic
search_input = driver.find_element(By.XPATH, "//input[@id='search']")
search_input.send_keys("positive")
search_input.send_keys(Keys.RETURN) # pressing enter

# infra
driver.quit()