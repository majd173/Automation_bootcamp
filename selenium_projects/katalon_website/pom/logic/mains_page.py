from selenium.katalon_website.pom.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Katalon_Mains(BasePage):
    OPEN_MENU_BUTTON = "//a[@id = 'menu-toggle']"
    MAKE_APPOINTMENT = "//a[@id =  'btn-make-appointment']"
    USER_NAME_INPUT = "//input[@name = 'username']"
    PASSWORD_INPUT = "//input[@name = 'password']"
    LOG_IN_BUTTON = "//button[@id = 'btn-login']"

    def __init__(self, driver):
        super().__init__(driver)
        self._open_menu_button = self._driver.find_element(By.XPATH, self.OPEN_MENU_BUTTON)
        self._make_appointment = self._driver.find_element(By.XPATH, self.MAKE_APPOINTMENT)
        self._user_name_input = self._driver.find_element(By.XPATH, self.USER_NAME_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._log_in_button = self._driver.find_element(By.XPATH, self.LOG_IN_BUTTON)

    def open_menu(self):
        self._open_menu_button.click()

    def click_appointment_button(self):
        self._make_appointment.click()

    def insert_username_check(self):
        self._user_name_input.send_keys('username')

    def insert_password_check(self):
        self._password_input.send_keys('password')


    