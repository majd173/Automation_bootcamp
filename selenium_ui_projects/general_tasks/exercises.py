import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains as AC

class TestSolnet(unittest.TestCase):

    def test_drag_and_drop(self):
        driver = webdriver.Chrome()
        driver.get('https://www.solnet.co.il/klondike3')
        driver.implicitly_wait(12)

        # Perform drag and drop
        first_element = driver.find_element(By.XPATH, "//div[@id = 'card18']")
        second_element = driver.find_element(By.XPATH, "//div[@id = 'card32']")
        action = AC(driver)
        action.drag_and_drop(first_element, second_element).perform()

        # Ensure that the page has been updated and the table is available
        driver.implicitly_wait(5)

        # Find and print table data
        try:
            table = driver.find_element(By.TAG_NAME, 'table')
            rows = table.find_elements(By.TAG_NAME, 'tr')
            for row in rows:
                cols = row.find_elements(By.TAG_NAME, 'td')
                for col in cols:
                    print(col.text, end="\t")
                print()
        except Exception as e:
            print(f"An error occurred: {e}")

        # Close the browser
        driver.quit()

if __name__ == "__main__":
    unittest.main()
