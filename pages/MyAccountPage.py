import logging
import re
import time
from playwright.sync_api import Page, expect
from pages.BasicPage import BasicPage


class MyAccountPage(BasicPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._locators = {"Home-btn": 'text="Return to Home"',
                          "account_name": 'xpath=//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span',
                          "error1": '//*[@id="center_column"]/div[1]/ol/li/text()'}

    def home(self):
        self._page.locator(*self._locators["Home-btn"]).click()
        return self._page

    def get_account_name(self):
        return self._page.locator(self._locators["account_name"]).text_content()

    def quit(self):
        self._page.close()

    def find_error(self):
        return self._page.locator(self._locators["error1"]).inner_text()
