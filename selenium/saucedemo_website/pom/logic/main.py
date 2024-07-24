from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.saucedemo_website.pom.infra.base_page import BasePage


class Main(BasePage):
    CART_TOGO = "//a[@class = 'shopping_cart_link']"
    MENU = "//button[@id = 'react-burger-menu-btn']"
    HEADER = "//div[@class = 'app_logo']"
    FOOTER = "//footer[@class = 'footer']"
    SAUCE_BACK_PACK = "//button[@id='add-to-cart-sauce-labs-backpack']"
    SAUCE_LABS_BIKE_LIGHT = "//button[@id = 'add-to-cart-sauce-labs-bike-light']"
    SAUCE_LABS_BOLT_T_SHIRT = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"

    def __init__(self, driver):
        super().__init__(driver)
        self._cart_togo = self._driver.find_element(By.XPATH, self.CART_TOGO)
        self._menu = self._driver.find_element(By.XPATH, self.MENU)
        self._header = self._driver.find_element(By.XPATH, self.HEADER)
        self._footer = self._driver.find_element(By.XPATH, self.FOOTER)
        self._sauce_back_pack = self._driver.find_element(By.XPATH, self.SAUCE_BACK_PACK)
        self._sauce_labs_bike_light = self._driver.find_element(By.XPATH, self.SAUCE_LABS_BIKE_LIGHT)
        self._sauce_labs_bolt_t_shirt = self._driver.find_element(By.XPATH, self.SAUCE_LABS_BOLT_T_SHIRT)

    def check_header(self):
        header_text = self._header.text
        print(header_text)

    def check_footer(self):
        print("footer exists")
        return self._footer

    def test_go_to_cart(self):
        self._cart_togo.click()

    def test_open_menu(self):
        self._menu.click()

    def click_sauce_back_pack(self):
        self._sauce_back_pack.click()

    def click_sauce_labs_bike_light(self):
        self._sauce_labs_bike_light.click()


    def click_sauce_labs_bolt_t_shirt(self):
        self._sauce_labs_bolt_t_shirt.click()
