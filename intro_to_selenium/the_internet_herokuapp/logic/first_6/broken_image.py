from intro_to_selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By


class BrokenImage(BasePage):
    IMG_ONE = "//*[@id='content']/div/img[1]"
    IMG_TWO = "//*[@id='content']/div/img[2]"
    IMG_THREE = "//*[@id='content']/div/img[3]"

    def __init__(self, driver):
        super().__init__(driver)
        self._img_one = self._driver.find_element(By.XPATH, self.IMG_ONE)
        self._img_two = self._driver.find_element(By.XPATH, self.IMG_TWO)
        self._img_three = self._driver.find_element(By.XPATH, self.IMG_THREE)

    def check_picture_display(self):
        print(self._img_one.is_displayed())
        print(self._img_two.is_displayed())
        print(self._img_three.is_displayed())

