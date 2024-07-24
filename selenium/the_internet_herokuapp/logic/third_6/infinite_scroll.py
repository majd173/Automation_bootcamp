import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class InfiniteScroll(BasePage):

    TEXT = "//div[@class='jscroll-added']"

    def __init__(self, driver):
        super().__init__(driver)
        self._text = self._driver.find_element(By.XPATH, self.TEXT)


    def scroll_down(self):
        text_appear = WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.TEXT)))
        try:
            if text_appear.is_displayed():
                print("text appeared...")
                actions = AC(self._driver)
                actions.send_keys(Keys.PAGE_DOWN).perform()
            else:
                print("text did not appear")
        except TimeoutException:
            print("Timeout: Text did not appear within the given time")

    def infinite_scroll(self, scroll_pause_time=2, max_scrolls=4):
        last_height = self._driver.execute_script("return document.body.scrollHeight")

        for i in range(max_scrolls):
            self.scroll_down()
            time.sleep(scroll_pause_time)
            new_height = self._driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

