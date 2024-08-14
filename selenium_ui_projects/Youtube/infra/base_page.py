class BasePage:

    def __init__(self, driver):
        self._driver = driver

    def return_page(self):
        self._driver.refresh()

    def get_current_url(self):
        return self._driver.current_url

    def get_title(self):
        return self._driver.title()
