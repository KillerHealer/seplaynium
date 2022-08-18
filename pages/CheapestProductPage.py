import time
from playwright.sync_api import Page
from pages.BasicPage import BasicPage


class CheapestProductPage(BasicPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._locators = {"add-to-cart": "text=Add to cart",
                          "proceed1": "text='Proceed to checkout'",
                          "proceed2": "#center_column >> text='Proceed to checkout'",
                          "proceed3": "button >> text='Proceed to checkout'",
                          "proceed4": "input#cgv",
                          "proceed5": "button >> text='Proceed to checkout'",
                          "proceed6": "text='Pay by bank wire'",
                          "proceed7": "button >> text='I confirm my order'",
                          "proceed8": 'body'}

    def buy(self):
        time.sleep(5)
        self._page.locator(self._locators["proceed1"]).click()
        time.sleep(2)
        self._page.locator(self._locators["proceed2"]).click()
        self._page.locator(self._locators["proceed3"]).click()
        checkbox = self._page.locator(self._locators["proceed4"])
        checkbox.click()
        self._page.locator(self._locators["proceed5"]).click()
        self._page.locator(self._locators["proceed6"]).click()
        self._page.locator(self._locators["proceed7"]).click()
        return self._page
