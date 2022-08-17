import logging
import re
import time
from playwright.sync_api import Page, expect


class BasicPage:
    def __init__(self, page: Page):
        self._page = page

    def current_url(self):
        return self._page.url
