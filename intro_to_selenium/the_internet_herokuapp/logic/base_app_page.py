from selenium.webdriver.chrome.webdriver import WebDriver
from intro_to_selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By
class BaseAppPage(BasePage): # includes common elements for all pages

    LOGO = "example"
    def __init__(self, driver):
        super().__init__(driver)
        self._logo = self._driver.find_element(By.XPATH, self.LOGO)


    def logo_is_displayed(self):
        return self._logo.is_displayed()