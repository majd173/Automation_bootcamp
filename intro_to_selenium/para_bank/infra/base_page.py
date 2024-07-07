class BasePage:


    def __init__(self, driver):
        self._driver = driver

    def return_page(self):
        self._driver.reload()

    def get_title(self):
        return self._driver.title()