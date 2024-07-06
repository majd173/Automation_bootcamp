from selenium.webdriver.common.action_chains import ActionChains as AC
from intro_to_selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class FloatingMen(BasePage):

    HOME = "//a[@href='#home']"


    def __init__(self, driver):
        super().__init__(driver)
        self._home = self._driver.find_element(By.XPATH, self.HOME)


    def scroll_down(self):
        actions = AC(self._driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        if self._home.is_displayed():
            print("home still appear")
        else:
            print("home does not appear")