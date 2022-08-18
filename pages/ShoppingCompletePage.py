import logging
import re
import time
from playwright.sync_api import Page, expect
from BasicPage import BasicPage


class ShoppingCompletePage(BasicPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._locators = {"body": "body"}

    def success(self):
        return self._page.locator(self._locators["body"]).inner_html() == "Your order on My Store is complete."
