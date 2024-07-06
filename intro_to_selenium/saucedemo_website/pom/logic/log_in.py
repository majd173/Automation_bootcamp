from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from intro_to_selenium.saucedemo_website.pom.infra.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogIn(BasePage):
    USER_NAME_INPUT = "//input[@id = 'user-name']"
    PASSWORD_INPUT = "//input[@id = 'password']"
    LOGIN_BUTTON = "//input[@id = 'login-button']"
    HEADER = "//div[@class = 'login_logo']"

    def __init__(self, driver):
        super().__init__(driver)
        self._user_name_input = self._driver.find_element(By.XPATH, self.USER_NAME_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        # self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)
        self._login_button = WebDriverWait(self._driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON)))
        self._header = self._driver.find_element(By.XPATH, self.HEADER)

    def fill_user_input(self, username):
        self._user_name_input.send_keys(username)

    def fill_password_input(self, password):
        self._password_input.send_keys(password)

    def click_login_button(self):
        self._login_button.click()

    def check_header(self):
        header_text = self._header.text
        print(header_text)

    def login_flow(self, username, password):
        self.fill_user_input(username)
        self.fill_password_input(password)
        self.click_login_button()



