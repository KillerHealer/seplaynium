import logging
import re
import time
from playwright.sync_api import Page, expect
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
        # product_list = self._page.locator(*self._locators["product_list"])
        # product_containers = product_list.(*self._locators["product_containers"])
        # minimum = 200.9
        # cheapest_product = self._page
        # for product_container in product_containers:
        #     right_block = product_container.find_element(*self._locators["right_block"])
        #     product_name = right_block.find_element(*self._locators["product_name"]).text
        #     if float(re.findall("\d+\.\d+", str(product_name))[0]) < minimum:
        #         minimum = float(re.findall("\d+\.\d+", str(product_name))[0])
        #         cheapest_product = product_container.find_element(*self._locators["cheapest_product"])
        # cheapest_product.click()
        # return self._driver
