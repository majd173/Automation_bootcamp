import json

from selenium import webdriver
from selenium_ui_projects.saucedemo_website.pom.infra .config_provider import ConfigProvider


class BrowserWrapper:
    # a class for managing a browser
    def __init__(self):
        self._driver = None # because I still don't know which driver to choose
        self.config = ConfigProvider.load_from_file('../config.json')

    # in this function we determine which browser to open and also opens it
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
            print("browser is not exist")

        self._driver.get(url)
        self._driver.maximize_window()
        return self._driver
