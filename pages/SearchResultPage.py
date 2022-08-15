import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.BasicPage import BasicPage


class SearchResultPage(BasicPage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self._locators = {"product_list": (By.CLASS_NAME, "product_list"),
                          "product_containers": (By.CLASS_NAME, "product-container"),
                          "right_block": (By.CLASS_NAME, "right-block"),
                          "product_name": (By.TAG_NAME, "span"),
                          "cheapest_product": (By.XPATH, '//*[@id="center_column"]/ul/li[3]')}

    def find_cheapest(self):
        product_list = self._driver.find_element(*self._locators["product_list"])
        product_containers = product_list.find_elements(*self._locators["product_containers"])
        minimum = 200.9
        cheapest_product = self._driver
        for product_container in product_containers:
            right_block = product_container.find_element(*self._locators["right_block"])
            product_name = right_block.find_element(*self._locators["product_name"]).text
            if float(re.findall("\d+\.\d+", str(product_name))[0]) < minimum:
                minimum = float(re.findall("\d+\.\d+", str(product_name))[0])
                cheapest_product = product_container.find_element(*self._locators["cheapest_product"])
        cheapest_product.click()
        return self._driver
