import logging
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By



class DownloadAppPage(BasePage):
    # This class manages the HomePage of the website.

    PREVIEW_BUTTON = "//a[@class='feature f-graphics pswp-link']"
    EARTH_IMAGE = "//div//div//img[@src='/images/screenshots/sss3_screenshot_05.jpg']"
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

    #------------------------------------------------------------------------------------------------------------
    # This function clicks on the preview button.
    def click_preview_button(self):
        self._preview_button.click()

    #------------------------------------------------------------------------------------------------------------
    # This function returns if the earth image is displayed.
    def earth_image_display(self):
        self._earth_image = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.EARTH_IMAGE)))
        if self._earth_image.is_displayed():
            logging.info("FEATURES VIEW IS DISPLAYED.")
            self._driver.save_screenshot('Features view display.png')
            return True
        logging.error("FEATURES VIEW IS NOT DISPLAYED")

    #------------------------------------------------------------------------------------------------------------
    # This function clicks on the "Show" button in the home page.
    def click_on_show_button(self):
        self._driver.execute_script("arguments[0].scrollIntoView();", self._show_button)
        self._driver.save_screenshot('Before clicking Show button.png')
        self._show_button.click()

    #------------------------------------------------------------------------------------------------------------
    # This function returns if the "Purchases steps tab" opens.
    def purchase_steps_opening(self):
        self._purchase_steps = WebDriverWait(self._driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.OPENED_STEPS)))
        self._driver.execute_script("arguments[0].scrollIntoView();", self._purchase_steps)
        if self._purchase_steps.is_displayed():
            logging.info("PURCHASE STEPS ARE OPENED.")
            self._driver.save_screenshot('After opening Purchase steps list.png')
            return True
        logging.info("PURCHASE STEPS ARE NOT OPENED.")
    #------------------------------------------------------------------------------------------------------------
