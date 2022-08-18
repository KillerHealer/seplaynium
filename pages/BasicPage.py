from selenium import webdriver


class BasicPage:
    def __init__(self, driver: webdriver):
        self._driver = driver

    def current_url(self):
        return self._driver.current_url
