from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# infra
driver = webdriver.Chrome()  # Chrome() is a constructor that initializes (opens) a chrome web-browser

# infra    # logic
driver.get('https://www.google.com')

# logic
search_input = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search_input.send_keys("Python programing", Keys.RETURN)
new_input = driver.find_element(By.XPATH, "//span[@dir = 'ltr']")
print("the first link is: ", new_input.text)
print("Test passed")
# search_input.send_keys(Keys.RETURN) # pressing enter

# infra
driver.quit()

