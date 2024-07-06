from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC




class HorizontalSlider(BasePage):

    SLIDER = "//input[@type='range']"
    VALUE = "//span[@id='range']"
    EXP_VALUE = "//span[text()='2.5']"


    def __init__(self, driver):
        super().__init__(driver)
        self._slider = self._driver.find_element(By.XPATH, self.SLIDER)
        self._value = self._driver.find_element(By.XPATH, self.VALUE)


    def move_slider(self):
        actions = AC(self._driver)
        actions.click_and_hold(self._slider).move_to_element(self._slider).release().perform()
        exp_value = WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.EXP_VALUE)))
        exp_value_text = exp_value.text

        if exp_value.is_displayed():
            print(f'{exp_value.is_displayed()}, value changed successfully to {exp_value_text}')
        else:
            print("value did not changed")
