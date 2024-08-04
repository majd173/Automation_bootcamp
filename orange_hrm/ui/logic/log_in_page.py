from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from orange_hrm.ui.infra.base_page import BasePage
from orange_hrm.ui.infra.config_provider import ConfigProvider


class LogInPage(BasePage):
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[type='password']"
    LOGIN_BUTTON = "button[type='submit']"

    def __init__(self, driver):
        super().__init__(driver)
        self._config = ConfigProvider.load_from_file(
            r'C:\Users\Admin\Desktop\Automation_bootcamp\orange_hrm\orange_hrm.json')
        self._wait = WebDriverWait(self._driver, 10)

    def insert_username(self):
        username_input = self._wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.USERNAME_INPUT)))
        username_input.send_keys(self._config["username"])

    def insert_password(self):
        password_input = self._wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.PASSWORD_INPUT)))
        password_input.send_keys(self._config["password"])

    def click_log_in_button(self):
        login_button = self._wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.LOGIN_BUTTON)))
        login_button.click()

    def login_flow(self):
        self.insert_username()
        self.insert_password()
        self.click_log_in_button()
        cookies = self._driver.get_cookies()
        return f'orangehrm={cookies[0]['value']}'
