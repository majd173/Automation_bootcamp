from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_ui_projects.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains as AC


class Hovers(BasePage):
    IMG_ONE = "//*[@id='content']/div/div[1]/img"
    USER_NAME = "//h5[text()='name: user1']"
    IMG_ONE_PROFILE = "//a[@href='/users/1']"
    NOT_FOUND = "//h1[text()='Not Found']"

    def __init__(self, driver):
        super().__init__(driver)
        self._img_one = self._driver.find_element(By.XPATH, self.IMG_ONE)

    def show_details(self):
        actions = AC(self._driver)
        actions.move_to_element(self._img_one).perform()
        user_name = WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.USER_NAME)))
        if user_name.is_displayed():
            print(f'{user_name.is_displayed()} user name appeared')
        else:
            print(f'{not user_name.is_displayed()} user name did not appeared')
        profile = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.IMG_ONE_PROFILE)))
        profile.click()
        not_found = WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.NOT_FOUND)))
        if not_found.is_displayed():
            print(f'{not_found.is_displayed()} you got the page')
        else:
            print(f'{not not_found.is_displayed()} you did not get the page')
