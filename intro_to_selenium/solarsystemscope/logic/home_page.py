from intro_to_selenium.solarsystemscope.infra.utils import Utils
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
import logging


class HomePage(BasePage):
    # This class manages the HomePage of the website.

    ACCOUNT_BUTTON = "//a[contains(text(), 'Account')]"
    EMAIL_INPUT = "//input[@placeholder='Your e-mail']"
    PASSWORD_INPUT = "//input[@placeholder='Your password']"
    LOGIN_BUTTON = "//button[contains(text(),'Login')]"
    DOWNLOAD_APP = "//a[@class='btn-type-3-green download hidden-xs only-dsk ']"
    EXPLORE_BUTTON = "//a[@class='btn-type-1-blue menu-hover-start-button']"
    ASTRONOMY_PLACES_BUTTON = "//a[@class='menu-hover-button main places']"
    ONLINE_APPS_BUTTON = "//a[@class='menu-hover-button main models only-dsk']"
    LOGOUT_BUTTON = "//a[@class='button account-logout']"
    ERROR_LOGIN_MESSAGE = "//div[contains(text(), 'Error:Email or password does not exist.')]"
    LIKE_BUTTON = "//a[@class='panel-type-10-semi-black-bg like']"
    LIKE_COUNT_BOX = "//span[@class='like-count']"


    def __init__(self, driver):
        super().__init__(driver)
        self._config = ConfigProvider.load_from_file("../solar_config.json")
        try:
            self._account_button = self._driver.find_element(By.XPATH, self.ACCOUNT_BUTTON)
        except NoSuchElementException:
            logging.error("ACCOUNT ELEMENT CAN NOT BE FOUND")

        try:
            self._like_button = self._driver.find_element(By.XPATH, self.LIKE_BUTTON)
        except NoSuchElementException:
            logging.error("LIKE ELEMENT CAN NOT BE FOUND")

        try:
            self._download_app = self._driver.find_element(By.XPATH, self.DOWNLOAD_APP)
        except NoSuchElementException:
            logging.error("DOWNLOAD ELEMENT CAN NOT BE FOUND")

        try:
            self._explore_button = self._driver.find_element(By.XPATH, self.EXPLORE_BUTTON)
        except NoSuchElementException:
            logging.error("EXPLORE ELEMENT CAN NOT BE FOUND")


    # ------------------------------------------------------------------------------------------------------------
    # This function clicks on the "Account" button.
    def click_account_button(self):
        self._account_button.click()
        logging.info("ACCOUNT BUTTON WAS CLICKED.")

    # ------------------------------------------------------------------------------------------------------------
    # This function inserts Email address in the input bar.
    def insert_email(self, input):
        self._email_input = WebDriverWait(self._driver, 7).until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT)))
        self._email_input.send_keys(input)
        logging.info("EMAIL ADDRESS WAS INSERTED.")

    # ------------------------------------------------------------------------------------------------------------
    # This function inserts password in the input bar.
    def insert_password(self, input):
        self._password_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.PASSWORD_INPUT)))
        self._password_input.send_keys(input)
        logging.info("PASSWORD WAS INSERTED.")

    # ------------------------------------------------------------------------------------------------------------
    # This function clicks on the "Login" button.
    def click_log_in_button(self):
        self._click_login_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LOGIN_BUTTON)))
        self._click_login_button.click()
        logging.info("LOGIN BUTTON WAS CLICKED..")

    # ------------------------------------------------------------------------------------------------------------
    # This function submits a full valid login process.
    def valid_log_in_flow(self):
        self.click_account_button()
        self.insert_email(self._config["valid_email"])
        self.insert_password(self._config["valid_password"])
        self.click_log_in_button()

    # ------------------------------------------------------------------------------------------------------------
    # This function submits a full invalid "Login" process.
    def invalid_log_in_flow(self):
        self._account_button.click()
        self.insert_email(self._config["invalid_email"])
        self.insert_password(Utils.generate_random_number(7))
        self.click_log_in_button()

    # ------------------------------------------------------------------------------------------------------------
    # This function returns if the "Logout" button is displayed.
    def logout_button_display(self):
        self._logout_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LOGOUT_BUTTON)))
        if self._logout_button.is_displayed():
            logging.info("YOU ARE LOGGED IN.")
            return True
        else:
            logging.error("YOU ARE STILL LOGGED IN.")

    # ------------------------------------------------------------------------------------------------------------
    # This function returns an invalid login message.
    def error_login_message_display(self):
        self._error_message = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ERROR_LOGIN_MESSAGE)))
        if self._error_message.is_displayed():
            logging.info("INVALID LOGIN DETAILS WERE INSERTED.")
            return self._error_message.text
        else:
            logging.error("AN ERROR OCCUERRED, INVALID ERROR MESSAGE MUST APPEAR.")

    # ------------------------------------------------------------------------------------------------------------
    # This function clicks on the "Logout" button.
    def click_on_logout_button(self):
        try:
            self._logout_button = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.LOGOUT_BUTTON)))
            self._logout_button.click()
            logging.info("LOGOUT BUTTON WAS CLICKED.")
        except NoSuchElementException:
            logging.error("LOGOUT ELEMENT CAN NOT BE FOUND.")

    # ------------------------------------------------------------------------------------------------------------
    # This function returns if the "Logout" button was clicked by displaying the
    #"Account" button.
    def logout_confirmation(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ACCOUNT_BUTTON)))
        if self._account_button:
            logging.info("YOU HAVE LOGGED OUT SUCCESSFULLY.")
            return True
        logging.error("YOU ARE STILL LOGGEN IN.")

    # ------------------------------------------------------------------------------------------------------------
    # This function clicks on the "Download App" button.
    def click_on_download_app(self):
        self._download_app.click()
        logging.info("DOWNLOAD APP BUTTON WAS CLICKED.")

    # ------------------------------------------------------------------------------------------------------------
    # This function clicks on the "Explore" button.
    def click_on_explore(self):
        self._explore_button.click()
        logging.info("EXPLORE BUTTON WAS CLICKED.")

    # ------------------------------------------------------------------------------------------------------------
    # This function clicks on the "Astronomy Places" button.
    def click_on_astronomy_places(self):
        try:
            self._astronomy_places = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.ASTRONOMY_PLACES_BUTTON)))
            self._astronomy_places.click()
            logging.info("ASTRONOMY PLACES BUTTON WAS CLICKED.")
        except NoSuchElementException:
            logging.error("ASTRONOMY PLACES ELEMENT CAN NOT BE FOUND.")

    # ------------------------------------------------------------------------------------------------------------
    # This function clicks on the "Online Apps" button.
    def click_on_online_apps_button(self):
        try:
            self._online_apps = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.ONLINE_APPS_BUTTON)))
            self._online_apps.click()
            logging.info("ONLINE APPS BUTTON WAS CLICKED.")
        except NoSuchElementException:
            logging.error("ONLINE APPS ELEMENT CAN NOT BE FOUND.")

    # ------------------------------------------------------------------------------------------------------------
    # This function clicks on the "Like" button.
    def click_on_like_button(self):
        self._driver.execute_script("arguments[0].scrollIntoView();", self._like_button)
        self._like_button.click()
        logging.info("LIKE BUTTON WAS CLICKED.")

    #------------------------------------------------------------------------------------------------------------
    # This function returns if the "Like" button is clickable
    # by returning if it is can be clicked after being clicked.
    def check_like_button_activity(self):
        try:
            self._like_count_box = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.LIKE_COUNT_BOX)))
            if self._like_count_box.is_displayed():
                logging.info("LIKE BUTTON IS NOT DISPLAYED AND CLICKABLE MORE.")
                return True
            logging.error("LIKE BUTTON WAS NOT CLICKED.")
            return False
        except NoSuchElementException:
            logging.error("LIKE ACCOUNT BOX ELEMENT CAN NOT BE FOUND.")

    #------------------------------------------------------------------------------------------------------------
