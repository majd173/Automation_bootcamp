from selenium.webdriver.common.by import By
from intro_to_selenium.the_internet_herokuapp.infra.base_page import BasePage
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class DisappearingElements(BasePage):
    GALLERY = "//a[@href='/gallery/']"

    def __init__(self, driver):
        super().__init__(driver)
        self._gallery = self._driver.find_element(By.XPATH, self.GALLERY)

    def check_gallery_apperance(self):
        if self._gallery.is_displayed():
            logging.info("True")
        else:
            logging.info("False")
        return

