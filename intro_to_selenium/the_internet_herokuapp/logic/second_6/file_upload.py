from basepage import wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By


class FileUpload(BasePage):

    FILE_UPLOAD = r"C:\Users\Admin\Pictures\Screenshots\4.8_flowchart1"
    CHOOSE_BTN = "//input[@id='file-upload']"
    UPLOAD_BTN = "//input[@id='file-submit']"
    MSG = "//*[@id='content']/div/h3"
    def __init__(self, driver):
        super().__init__(driver)
        self._choose_btn = self._driver.find_element(By.XPATH, self.CHOOSE_BTN)
        self._upload_btn = self._driver.find_element(By.XPATH, self.UPLOAD_BTN)

    def upload_file(self):
        self._choose_btn.click()
        self._driver.send_keys(self.FILE_UPLOAD)
        self._driver.find_element(By.NAME, "Open").click()
        self._upload_btn.click()
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "File Uploaded!")))


