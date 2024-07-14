import json
import logging
from selenium import webdriver
from intro_to_selenium.saucedemo_website.pom.infra.config_provider import ConfigProvider


class BrowserWrapper:
    # This class manages choosing a browser.
    def __init__(self):
        self._driver = None # because I still don't know which driver to choose.
        self.config = ConfigProvider.load_from_file('../solar_config.json')
    # ------------------------------------------------------------------------------------------------------------
    # This function determines which browser to open and also opens it.
    def get_driver(self):
        url = self.config.get("base_url")
        if not url:
            raise ValueError("URL not found in the configuration.")
        if self.config["browser"] == "Chrome":
            self._driver = webdriver.Chrome()
        elif self.config["browser"] == "FireFox":
            self._driver = webdriver.Firefox()
        elif self.config["browser"] == "Edge":
            self._driver = webdriver.Edge()
        else:
            logging.error("")

        self._driver.get(url)
        self._driver.maximize_window()
        logging.info(f'Opens: {self.config["browser"]} browser')
        return self._driver
