import logging
import unittest
import time
from intro_to_selenium.para_bank.infra.config_provider import ConfigProvider
from intro_to_selenium.para_bank.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.Youtube.logic.home_page import HomePage
from intro_to_selenium.Youtube.logic.keyboard_shorcuts import KeyboardShortcutsConfirm


class TestKeyboardShortcuts(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file('../../solarsystemscope/config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)

    # opening the homepage before all tests

    def tearDown(self):
        self._driver.close()
    # closing the website after all tests

    def test_keyboard_shortcuts_display(self):
        print("Checking keyboard shortcuts display test began...")
        self.home_page.open_keyboard_shortcuts()
        pop_up_windows = KeyboardShortcutsConfirm(self._driver)
        self.assertTrue(pop_up_windows.confirm_keyboard_shortcuts_pop_up_window())
        time.sleep(3) # In order to confirm the display of keyboard shortcuts pop up windows
        print("--------------------------------------------")
        # tests the display of keyboard shortcuts.