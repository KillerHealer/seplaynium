from pages.BasicPage import BasicPage
from selenium import webdriver
from selenium.webdriver.common.by import By


class ShoppingCompletePage(BasicPage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self._locators = {"Home-btn": (By.LINK_TEXT, "home"),
                          "blabla": (By.LINK_TEXT, "jnk")}

    def success(self):
        return self._driver.find_element(By.CLASS_NAME, "cheque-indent").text == "Your order on My Store is complete."