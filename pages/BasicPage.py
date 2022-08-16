from selenium import webdriver
from selenium.webdriver.common.by import By


class BasicPage:
    def __init__(self, driver: webdriver):
        self._driver = driver

    def current_url(self):
        return self._driver.current_url

    # def find_element_and_color_it(self, by: By, this: str):
    #     pass