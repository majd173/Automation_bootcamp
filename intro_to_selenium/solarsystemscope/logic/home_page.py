import logging
import time
from intro_to_selenium.solarsystemscope.infra.utils import Utils
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class HomePage(BasePage):
    ACCOUNT_BUTTON = "(//a[@href='/login'])[1]"
    EMAIL_INPUT = "//input[@placeholder='Your e-mail']"
    PASSWORD_INPUT = "//input[@placeholder='Your password']"
    LOGIN_BUTTON = "//button[contains(text(),'Login')]"
    DOWNLOAD_APP = "//a[@class='btn-type-3-green download hidden-xs only-dsk ']"
    EXPLORE_BUTTON = "//a[@class='btn-type-1-blue menu-hover-start-button']"
    ASTRONOMY_PLACES_BUTTON = "(//a[@href='/places'])[1]"
    FACEBOOK_BUTTON = "(//a[@href='https://www.facebook.com/SolarSystemScopeModels/'])[1]"
    GERMAN_PAGE_BUTTON = "(//a[@href='https://solarsystemscope.de/'])[1]"
    YOUTUBE_PAGE_BUTTON = "(//a[@href='https://youtu.be/0pYMy1XsvFY'])[1]"
    GOOGLE_PLAY_PAGE = "(//a[@href='https://play.google.com/store/apps/details?id=air.com.eu.inove.sss2'])[2]"
    ONLINE_APPS_BUTTON = "(//a[@href='/models'])[1]"
    LOGOUT_BUTTON = "//a[@class='button account-logout']"
    ERROR_LOGIN_MESSAGE = "//div[contains(text(), 'Error:Email or password does not exist.')]"
    MERCHANDISE_BUTTON = "(//a[@href='https://shop.spreadshirt.com/solarsystemscope/'])[1]"
    EMBEDDING_BUTTON = "(//a[@href='/embed'])[2]"
    LIKE_BUTTON = "//a[@class='panel-type-10-semi-black-bg like']"

    def __init__(self, driver):
        super().__init__(driver)
        self._config = ConfigProvider.load_from_file("../config.json")
        try:
            self._account_button = self._driver.find_element(By.XPATH, self.ACCOUNT_BUTTON)
        except NoSuchElementException:
            logging.error("ACCOUNT ELEMENT CAN NOT BE FOUND")

        try:
            self._like_button = self._driver.find_element(By.XPATH, self.LIKE_BUTTON)
        except NoSuchElementException:
            logging.error("LIKE ELEMENT CAN NOT BE FOUND")

    # ------------------------------------------------------------------------------------------------------------

    def click_account_button(self):
        self._account_button.click()

    # ------------------------------------------------------------------------------------------------------------

    def insert_email(self, input):
        self._email_input = WebDriverWait(self._driver, 7).until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT)))
        self._email_input.send_keys(input)

    # ------------------------------------------------------------------------------------------------------------

    def insert_password(self, input):
        self._password_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.PASSWORD_INPUT)))
        self._password_input.send_keys(input)

    # ------------------------------------------------------------------------------------------------------------

    def click_log_in_button(self):
        self._click_login_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LOGIN_BUTTON)))
        self._click_login_button.click()

    # ------------------------------------------------------------------------------------------------------------

    def valid_log_in_flow(self):
        self.click_account_button()
        time.sleep(2)
        self.insert_email(self._config["valid_email"])
        self.insert_password(self._config["valid_password"])
        self.click_log_in_button()
        time.sleep(4)

    # ------------------------------------------------------------------------------------------------------------

    def invalid_log_in_flow(self):
        self.click_account_button()
        time.sleep(2)
        self.insert_email(self._config["invalid_email"])
        self.insert_password(Utils.generate_random_number(7))
        self.click_log_in_button()
        time.sleep(2)

    # ------------------------------------------------------------------------------------------------------------

    def logout_button_display(self):
        self._logout_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LOGOUT_BUTTON)))
        if self._logout_button.is_displayed():
            return True
        else:
            logging.error("YOU ARE STILL NOT LOGGED IN.")

    # ------------------------------------------------------------------------------------------------------------

    def error_login_message_display(self):
        self._error_message = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ERROR_LOGIN_MESSAGE)))
        if self._error_message.is_displayed():
            logging.info("INVALID LOGIN DETAILS WERE INSERTED.")
            return self._error_message.text
        else:
            logging.error("AN ERROR OCCUERRED, ERROR MESSAGE SHOULD APPEAR.")

    # ------------------------------------------------------------------------------------------------------------

    def click_on_logout_button(self):
        try:
            self._logout_button = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.LOGOUT_BUTTON)))
            self._logout_button.click()
            time.sleep(2)
        except NoSuchElementException:
            logging.error("LOGOUT ELEMENT CAN NOT BE FOUND.")

    # ------------------------------------------------------------------------------------------------------------

    def logout_confirmation(self):
        if self._account_button:
            logging.info("YOU HAVE LOGGED OUT SUCCESSFULLY.")
            return True
        logging.error("YOU ARE STILL LOGGEN IN.")

    # ------------------------------------------------------------------------------------------------------------

    def click_on_download_app(self):
        try:
            self._download_app = WebDriverWait(self._driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, self.DOWNLOAD_APP)))
            self._download_app.click()
        except NoSuchElementException:
            logging.info("DOWNLOAD ELEMENT CAN NOT BE FOUND.")

    # ------------------------------------------------------------------------------------------------------------

    def click_on_explore(self):
        try:
            self._explore = WebDriverWait(self._driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, self.EXPLORE_BUTTON)))
            self._explore.click()
        except NoSuchElementException:
            logging.info("EXPLORE ELEMENT CAN NOT BE FOUND")
        time.sleep(2)

    # ------------------------------------------------------------------------------------------------------------

    def click_on_astronomy_places(self):
        try:
            self._astronomy_places = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.ASTRONOMY_PLACES_BUTTON)))
            self._astronomy_places.click()
            time.sleep(2)
        except NoSuchElementException:
            logging.error("ASTRONOMY PLACES ELEMENT IS NOT FOUND.")

    # ------------------------------------------------------------------------------------------------------------

    def click_on_google_play_button(self):
        try:
            self._google_play_page_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.GOOGLE_PLAY_PAGE)))
            self._google_play_page_button.click()
        except NoSuchElementException:
            logging.error("GOOGLE PLAY PAGE ELEMENT CAN NOT BE FOUND.")
            time.sleep(4)

    # ------------------------------------------------------------------------------------------------------------

    def click_on_online_apps_button(self):
        try:
            self._online_apps = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.ONLINE_APPS_BUTTON)))
            self._online_apps.click()
            time.sleep(2)
        except NoSuchElementException:
            logging.error("ONLINE APPS ELEMENT CAN NOT FOUND.")

    # ------------------------------------------------------------------------------------------------------------

    def click_on_like_button(self):
        time.sleep(3)
        self._like_button.click()
        time.sleep(3)

    #------------------------------------------------------------------------------------------------------------

    def check_like_button_activity(self):
        try:
            self._like_button.click()
            WebDriverWait(self._driver, 5).until_not(EC.element_to_be_clickable(self._like_button))
            return True
        except WebDriverException:
            print("ELEMENT IS NOT CLICKABLE.")
            return True

    #------------------------------------------------------------------------------------------------------------
