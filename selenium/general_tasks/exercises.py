import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains as AC

class TestSolnet(unittest.TestCase):


    def test_drag_and_drop(self):
        driver = webdriver.Chrome()
        driver.get('https://www.solnet.co.il/klondike3')
        driver.implicitly_wait(12)
        first_element = driver.find_element(By.XPATH, "//div[@id = 'card18']")
        second_element = driver.find_element(By.XPATH, "//div[@id = 'card32']")
        action = AC(driver)
        action.drag_and_drop(first_element, second_element).perform()
        driver.quit()


        table = driver.find_element_by_tag_name("table1")
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            cols = row.find_element_by_tag_name("td")
            for col in cols:
                print(col.text + "\t, end = "")
            print( )
        driver.quit()




