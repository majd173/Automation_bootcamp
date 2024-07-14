import logging
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage



class EretzMuseumPage(BasePage):
    # This class manages the "Eretz Museum" website page.

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver

    #------------------------------------------------------------------------------------------------------------


