from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.BasicPage import BasicPage


class MyAccountPage(BasicPage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self._locators = {"Home-btn": (By.CLASS_NAME, "home"),
                          "account-name": (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span'),
                          "find-error1": (By.XPATH, '//*[@id="center_column"]/div[1]'),
                          "find-error2": (By.XPATH, '//*[@id="center_column"]/div[1]/ol/li')}

    def home(self):
        self._driver.find_element(*self._locators["Home-btn"]).click()
        return self._driver

    def get_account_name(self):
        return self._driver.find_element(*self._locators["account-name"]).text

    def quit(self):
        self._driver.quit()

    def find_error(self):
        return self._driver.find_element(*self._locators["find-error1"]) \
                 .find_element(*self._locators["find-error2"]).text
