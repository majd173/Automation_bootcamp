from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from intro_to_selenium.saucedemo_website.pom.infra.base_page import BasePage
from intro_to_selenium.saucedemo_website.pom.logic.main import Main


class Cart(BasePage):
    MENU = "//button[@id = 'react-burger-menu-btn']"
    HEADER = "//div[@class = 'app_logo']"
    FOOTER = "//footer[@class = 'footer']"
    SAUCE_BACK_PACK_EXIST = "//a[@id= 'item_4_title_link']"
    SAUCE_LABS_BIKE_LIGHT_EXIST = "//a[@id= 'item_0_title_link']"
    SAUCE_BACK_PACK_REMOVE = "//button[@id = 'remove-sauce-labs-backpack']"
    SAUCE_LABS_BIKE_LIGHT_REMOVE = "//button[@id = 'remove-sauce-labs-bike-light']"
    SAUCE_LABS_BOLT_T_SHIRT_REMOVE = "//button[@id = 'remove-sauce-labs-bolt-t-shirt']"

    def __init__(self, driver):
        super().__init__(driver)
        self._menu = self._driver.find_element(By.XPATH, self.MENU)
        self._header = self._driver.find_element(By.XPATH, self.HEADER)
        self._footer = self._driver.find_element(By.XPATH, self.FOOTER)
        self._sauce_back_pack_remove = self._driver.find_element(By.XPATH, self.SAUCE_BACK_PACK_REMOVE)
        self._sauce_labs_bike_light_remove = self._driver.find_element(By.XPATH, self.SAUCE_LABS_BIKE_LIGHT_REMOVE)
        self._sauce_labs_bolt_t_shirt_remove = self._driver.find_element(By.XPATH, self.SAUCE_LABS_BOLT_T_SHIRT_REMOVE)
        self._sauce_back_pack_exist = self._driver.find_element(By.XPATH, self.SAUCE_BACK_PACK_EXIST)
        self._sauce_labs_bike_light_exist = self._driver.find_element(By.XPATH, self.SAUCE_LABS_BIKE_LIGHT_EXIST)

    def remove_item(self, item_path):
        remove_item = self._driver.find_element(By.XPATH, item_path)
        remove_item.click()


    def check_items_exist(self):
        print(f'first item in the cart: {self._sauce_back_pack_exist.is_displayed()}\n'
              f'second item in the cart: {self._sauce_labs_bike_light_exist.is_displayed()}')
