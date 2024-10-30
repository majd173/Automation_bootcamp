from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestFlukeSearch(unittest.TestCase):

    def test_search(self):
        driver = webdriver.Chrome()
        driver.get('https://www.fluke.com/en-us?srsltid=AfmBOoqdAz_JTVjkfvsZmD-CjybNG0GtH4KR20qmIADznYVeIFnl7ffj')
        driver.maximize_window()
        search_input = (WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search Fluke']"))))
        search_button = (WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='alg-search-submit-search']"))))
        search_input.send_keys("positive")
        search_button.click()
        results = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'results')]"))
        )
        results_text = results.text
        self.assertIn("results", results_text)
