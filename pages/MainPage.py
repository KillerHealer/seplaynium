import logging
import re
import time
from playwright.sync_api import Page, expect
from BasicPage import BasicPage


class MainPage(BasicPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._locators = {"Sign-In": 'xpath=//*[@id="header"]/div[2]/div/div/nav/div[1]/a',
                          "search-box": "id=search_query_top",
                          "search-btn": "button.button-search"}

    def SignIn(self):
        self._page.locator(*self._locators["Sign-In"]).click()
        return self._page

    def search(self, search_word):
        self._page.locator(*self._locators["search-box"]).type(search_word)
        self._page.locator(*self._locators["search-btn"]).click()
        return self._page

