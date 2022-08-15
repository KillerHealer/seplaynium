from selenium import webdriver
from selenium.webdriver.common.by import By
from BasicPage import BasicPage


class MainPage(BasicPage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self._locators = {"Sign-In": (By.CLASS_NAME, "login"),
                          "search-box": (By.ID, "search_query_top"),
                          "search-btn": (By.NAME, "submit_search")}

    def SignIn(self):
        self._driver.find_element(*self._locators["Sign-In"]).click()
        return self._driver

    def search(self, search_word):
        self._driver.find_element(*self._locators["search-box"]).send_keys(search_word)
        self._driver.find_element(*self._locators["search-btn"]).click()
        return self._driver

