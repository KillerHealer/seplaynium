import time
from selenium.webdriver import ActionChains
from pages.BasicPage import BasicPage
from selenium import webdriver
from selenium.webdriver.common.by import By


class CheapestProductPage(BasicPage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self._locators = {"add-to-cart": (By.ID, "add_to_cart"),
                          "proceed1": (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a'),
                          "proceed2": (By.ID, "center_column"),
                          "proceed3": (By.CLASS_NAME, "cart_navigation"),
                          "proceed4": (By.CLASS_NAME, "button"),
                          "proceed5": (By.CLASS_NAME, "cart_navigation"),
                          "proceed6": (By.TAG_NAME, "button"),
                          "proceed7": (By.XPATH, '//*[@id="cgv"]'),
                          "proceed8": (By.NAME, "processCarrier"),
                          "proceed9": (By.CLASS_NAME, "bankwire"),
                          "proceed10": (By.ID, "center_column"),
                          "proceed11": (By.TAG_NAME, "button")}

    def buy(self):
        add_to_cart = self._driver.find_element(*self._locators["add-to-cart"])
        add_to_cart.click()
        time.sleep(8)
        self._driver.find_element(*self._locators["proceed1"]).click()
        proceed = self._driver.find_element(*self._locators["proceed2"]) \
            .find_element(*self._locators["proceed3"]).find_element(*self._locators["proceed4"])
        actions = ActionChains(self._driver)
        actions.move_to_element(proceed).click().perform()
        proceed = self._driver.find_element(*self._locators["proceed5"]).find_element(*self._locators["proceed6"])
        actions = ActionChains(self._driver)
        actions.move_to_element(proceed).click().perform()
        checkbox = self._driver.find_element(*self._locators["proceed7"])
        actions = ActionChains(self._driver)
        actions.move_to_element(checkbox).click().perform()
        proceed = self._driver.find_element(*self._locators["proceed8"])
        actions = ActionChains(self._driver)
        actions.move_to_element(proceed).click().perform()
        proceed = self._driver.find_element(*self._locators["proceed9"])
        actions = ActionChains(self._driver)
        actions.move_to_element(proceed).click().perform()
        proceed = self._driver.find_element(*self._locators["proceed10"]).find_element(*self._locators["proceed11"])
        actions = ActionChains(self._driver)
        actions.move_to_element(proceed).click().perform()
        return self._driver
