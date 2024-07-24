from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By


class FileDownload(BasePage):

    FILE_ONE = "//a[@href='download/pom.xml']"


    def __init__(self, driver):
        super().__init__(driver)
        self._file_one = self._driver.find_element(By.XPATH, self.FILE_ONE)


    def download_file(self):
        self._file_one.click()
        



