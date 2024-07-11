import logging
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class DownloadAppPage(BasePage):

    PREVIEW_BUTTON = "//a[@class='feature f-graphics pswp-link']"
    EARTH_IMAGE = "(//img[@src='/images/screenshots/sss3_screenshot_05.jpg'])[2]"
    SHOW_PURCHASE_STEPS_BUTTON = "//div[@class='arrow']"
    OPENED_STEPS = "//div[@class='steps-opened']"


    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._preview_button = self._driver.find_element(By.XPATH, self.PREVIEW_BUTTON)
        except NoSuchElementException:
            logging.error("PREVIEW BUTTON CAN NOT BE FOUND.")
        try:
            self._show_button = self._driver.find_element(By.XPATH, self.SHOW_PURCHASE_STEPS_BUTTON)
        except NoSuchElementException:
            logging.error("SHOW BUTTON CAN NOT BE FOUND.")


    def click_preview_button(self):
        self._preview_button.click()

    def earth_image_display(self):
        self._earth_image = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.EARTH_IMAGE)))
        if self._earth_image.is_displayed():
            logging.info("FEATURES VIEW IS DISPLAYED.")
            return True
        logging.error("FEATURES VIEW IS NOT DISPLAYED")

    def click_on_show_button(self):
        self._show_button.click()

    def purchase_steps_opening(self):
        self._purchase_steps = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.OPENED_STEPS)))
        if self._purchase_steps.is_displayed():
            print("PURCHASE STEPS ARE OPENED.")
            time.sleep(2)
            return True
        print("PURCHASE STEPS ARE NOT OPENED.")



