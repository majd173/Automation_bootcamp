import logging
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class FcebookPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def get_page_title(self, driver):
        return driver.title