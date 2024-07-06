from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By



class DynamicContent(BasePage):

    CLICK_HERE = "//*[@id='content']/div/p[2]/a"
    FIRST_CONT = "//*[@id='content']/div[1]/div[2]"
    SECOND_CONT = "//*[@id='content']/div[2]/div[2]"
    THIRD_CONT = "//*[@id='content']/div[3]/div[2]"


    def __init__(self, driver):
        super().__init__(driver)
        self._click_here = self._driver.find_element(By.XPATH, self.CLICK_HERE)


    def change_content(self):
        self._click_here.click()
        first_con = WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.FIRST_CONT)))
        second_con = WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.SECOND_CONT)))
        third_con = WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.THIRD_CONT)))

        print(first_con.is_displayed())
        print(second_con.is_displayed())
        print(third_con.is_displayed())




