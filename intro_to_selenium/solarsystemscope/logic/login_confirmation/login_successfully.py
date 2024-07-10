import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class LogInSuccessfully(BasePage):

    LOGOUT_BUTTON = "//a[@class='button account-logout']"


    def __init__(self, driver):
        super().__init__(driver)


    def logout_button_display(self):
        self._logout_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LOGOUT_BUTTON)))
        if self._logout_button.is_displayed():
            logging.info("YOU ARE LOGGED IN.")
            return True
        else:
            logging.error("YOU ARE STILL NOT LOGGED IN.")

