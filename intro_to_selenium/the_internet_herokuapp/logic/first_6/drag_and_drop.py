from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from intro_to_selenium.the_internet_herokuapp.infra.base_page import BasePage


class DragAndDrop(BasePage):

    A_BOX = "//*[@id='column-a']"
    B_BOX = "//*[@id='column-b']"

    def __init__(self, driver):
        super().__init__(driver)
        self._a_box = self._driver.find_element(By.XPATH, self.A_BOX)
        self._b_box = self._driver.find_element(By.XPATH, self.B_BOX)

    def drag_and_drop(self):
        actions = AC(self._driver)
        actions.click_and_hold(self._a_box).move_to_element(self._b_box).release().perform()