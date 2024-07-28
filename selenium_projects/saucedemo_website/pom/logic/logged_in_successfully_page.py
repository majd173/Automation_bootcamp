from selenium.webdriver.common.by import By
from selenium.saucedemo_website.pom.infra.base_page import BasePage


class LoggedInSuccessfully(BasePage):
    MENU = "//button[@id = 'react-burger-menu-btn']"

    def __init__(self, driver):
        super().__init__(driver)
        self._menu = self._driver.find_element(By.XPATH, self.MENU)

    def menu_is_exist(self):
        return self._menu.is_displayed()
