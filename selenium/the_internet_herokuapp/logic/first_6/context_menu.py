from selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC


class ContextMenu(BasePage):
    HOT_SPOT = "//div[@id= 'hot-spot']"

    def __init__(self, driver):
        super().__init__(driver)
        self._hot_spot = self._driver.find_element(By.XPATH, self.HOT_SPOT)

    def right_click_test(self):
        actions = AC(self._driver)
        actions.context_click(self._hot_spot).perform()
