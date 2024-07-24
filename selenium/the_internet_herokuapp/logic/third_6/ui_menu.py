from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC

class UiMenu(BasePage):

    ENABLED_BTN = "//a[text()='Enabled']"
    DOWNLOADS = "//a[text()='Downloads']"
    PDF = "//a[@href='/download/jqueryui/menu/menu.pdf']"

    def __init__(self, driver):
        super().__init__(driver)
        self._enabled_btn = self._driver.find_element(By.XPATH, self.ENABLED_BTN)


    def open_menu(self):
        self._enabled_btn.click()
        try:
            downloads = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.DOWNLOADS)))
            if downloads.is_displayed():
                print(f'{downloads.is_displayed()}, downloads appears')
            else:
                print("downloads bot appeared")
        except TimeoutException:
            print("Timeout: Text did not appear within the given time")

    def download_pdf(self):
        self.open_menu()
        downloads = WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.DOWNLOADS)))
        downloads.click()
        try:
            pdf = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.PDF)))
            if pdf.is_displayed():
                print(f'{pdf.is_displayed()}, pdf displayed')
                pdf.click()
                pdf_text = pdf.text
                print(f'{pdf_text} file was downloaded')
            else:
                print("pdf is not displayed")
        except TimeoutException:
            print("Timeout: Text did not appear within the given time")

        try:
            downloads_close = WebDriverWait(self._driver, 5).until(
                EC.invisibility_of_element_located((By.XPATH, self.DOWNLOADS)))
            if not downloads_close.is_displayed():
                print(f'{not downloads_close.is_displayed()}, downloads closed')
            else:
                print("download still opened...")
        except TimeoutException:
             print("error")

