import logging
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class EretzMuseumPage(BasePage):
    # This class manages the "Eretz Museum"website page.

    def __init__(self, driver):
        super().__init__(driver)

    #------------------------------------------------------------------------------------------------------------

    # This function returns the website's URL.
    def get_page_url(self):
        return self._driver.current_url
