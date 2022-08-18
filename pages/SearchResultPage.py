import logging
import re
from playwright.sync_api import Page
from BasicPage import BasicPage


class SearchResultPage(BasicPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._locators = {"product_list": 'ul.product_list li',
                          "prices": "ul.product_list li .product-price",
                          "add_to_cart": "text='Add to cart'"}

    def find_cheapest(self):
        products_list = self._page.locator(self._locators["product_list"])
        prices = self._page.locator(self._locators["prices"])
        prices_list = []
        for price in prices.all_inner_texts():
            prices_list.append(re.sub('[^\d\.]', "", price))
        cheapest_product = products_list.locator(f".product-container:has-text('${(min(prices_list))}')")
        cheapest_product.hover()
        logging.info("finding the cheapest product in the search page and starting to buy it!")
        self._page.wait_for_timeout(3000)
        cheapest_product.locator(self._locators["add_to_cart"]).click()
        return self._page

