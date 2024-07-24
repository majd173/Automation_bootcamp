from selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By


class DataTables(BasePage):

    TABLE = "//TABLE[@id='table1']"


    def __init__(self,driver):
        super().__init__(driver)
        self._table = self._driver.find_element(By.XPATH, self.TABLE)


    def print_elements(self):
        rows = self._table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, 'td')
            for col in cols:
                print(col.text + "\t", end="")
            print()