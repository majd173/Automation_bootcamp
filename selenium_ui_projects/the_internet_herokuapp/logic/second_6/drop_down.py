from selenium_ui_projects.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By



class DropDown(BasePage):

    DROP_DOWN = "//select[@id = 'dropdown']"
    OPTION_1 = "//option[@value='1']"
    OPTION_2 = "//option[@value='2']"

    def __init__(self, driver):
        super().__init__(driver)
        self._drop_down = self._driver.find_element(By.XPATH, self.DROP_DOWN)
        self._option_1 = self._driver.find_element(By.XPATH, self.OPTION_1)
        self._option_2 = self._driver.find_element(By.XPATH, self.OPTION_2)





    def drop_down(self):
        self._drop_down.click()
        print(self._option_1.is_displayed())
        print(self._option_2.is_displayed())


    def click_option_1(self):
        self._drop_down.click()
        self._option_1.click()
        print(self._option_1.is_displayed())


    def click_option_2(self):
        self._drop_down.click()
        self._option_2.click()
        print(self._option_2.is_displayed())




