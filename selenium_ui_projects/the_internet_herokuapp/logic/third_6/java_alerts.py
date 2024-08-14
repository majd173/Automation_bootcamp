from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_ui_projects.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class JavaAlerts(BasePage):

    JS_CONFIRM = "//button[@onclick='jsConfirm()']"
    CANCEL_CONFIRMATION = "//p[text()='You clicked: Cancel']"

    def __init__(self, driver):
        super().__init__(driver)
        self._js_confirm = self._driver.find_element(By.XPATH, self.JS_CONFIRM)


    def click_js(self):
        self._js_confirm.click()
        time.sleep(2)
        try:
            alert = self._driver.switch_to.alert
            alert.dismiss()
            cancel_confirmation = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.CANCEL_CONFIRMATION)))
            text = cancel_confirmation.text
            if cancel_confirmation.is_displayed():
                print(f'result: {text}')
            else:
                print("you chose ok")
        except NoAlertPresentException:
            print("No alert present")
        except TimeoutException:
            print("Timeout: Text did not appear within the given time")


