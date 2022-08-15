from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.BasicPage import BasicPage


class MyAccountPage(BasicPage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self._locators = {"Home-btn": (By.CLASS_NAME, "home"),
                          "blabla": (By.LINK_TEXT, "jnk")}

    def home(self):
        self._driver.find_element(*self._locators["Home-btn"]).click()
        return self._driver

    def current_url(self):
        return self._driver.current_url

    def get_account_name(self):
        return self._driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span').text

    def quit(self):
        self._driver.quit()
