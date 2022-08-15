import logging
import time
import pytest
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.AuthenticationPage import AuthenticationPage
from pages.CheapestProductPage import CheapestProductPage
from pages.MainPage import MainPage
from pages.MyAccountPage import MyAccountPage
from pages.SearchResultPage import SearchResultPage
from pages.ShoppingCompletePage import ShoppingCompletePage
from pages.BasicPage import BasicPage


@pytest.fixture()
def main_page():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrom_driver_path = "D:\pythonProject\chromedriver.exe"
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get("http://automationpractice.com/index.php")
    main_page = MainPage(driver)
    return main_page


def test_buy_cheapest_dress(main_page):
    """
    tries to find the cheapest dress from the search for summer and buys it
    :return:
    """
    authentication_page = AuthenticationPage(main_page.SignIn())
    my_account_page = MyAccountPage(authentication_page.login("noam@gmail.com", "Abcd1234@"))
    main_page = MainPage(my_account_page.home())
    search_result_page = SearchResultPage(main_page.search("summer"))
    cheapest_product_page = CheapestProductPage(search_result_page.find_cheapest())
    shopping_complete_page = ShoppingCompletePage(cheapest_product_page.buy())
    assert shopping_complete_page.success()
    shopping_complete_page._driver.close()
    # driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    # driver.maximize_window()
    # driver.get('http://automationpractice.com/index.php')
    # login_btn = driver.find_element(By.CLASS_NAME, "login")
    # login_btn.click()
    # logging.info("going from the home screen to the login screen!")
    # login_form = driver.find_element(By.XPATH, '//*[@id="login_form"]')
    # email_input = login_form.find_element(By.XPATH, '//*[@id="email"]')
    # email_input.send_keys("noam@gmail.com")
    # pass_input = login_form.find_element(By.XPATH, '//*[@id="passwd"]')
    # pass_input.send_keys("Abcd1234@")
    # sign_in_btn = login_form.find_element(By.XPATH, '//*[@id="SubmitLogin"]')
    # sign_in_btn.click()
    # logging.info("signing in!")
    # search_box = driver.find_element(By.ID, "search_query_top")
    # search_btn = driver.find_element(By.NAME, "submit_search")
    # search_box.send_keys("summer")
    # search_btn.click()
    # logging.info("searching for the word 'summer' in the search bar and going to the search page!")
    # time.sleep(4)
    # product_list = driver.find_element(By.CLASS_NAME, "product_list")
    # product_containers = product_list.find_elements(By.CLASS_NAME, "product-container")
    # minimum = 200.9
    # cheapest_product = driver
    # for product_container in product_containers:
    #     right_block = product_container.find_element(By.CLASS_NAME, "right-block")
    #     product_name = right_block.find_element(By.TAG_NAME, "span").text
    #     if float(re.findall("\d+\.\d+", str(product_name))[0]) < minimum:
    #         minimum = float(re.findall("\d+\.\d+", str(product_name))[0])
    #         cheapest_product = product_container.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[3]')
    # cheapest_product.click()
    # add_to_cart = driver.find_element(By.ID, "add_to_cart")
    # logging.info("finding the cheapest product in the search page and starting to buy it!")
    # add_to_cart.click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a').click()
    # proceed = driver.find_element(By.ID, "center_column")\
    #     .find_element(By.CLASS_NAME, "cart_navigation").find_element(By.CLASS_NAME, "button")
    # actions = ActionChains(driver)
    # actions.move_to_element(proceed).click().perform()
    # proceed = driver.find_element(By.CLASS_NAME, "cart_navigation").find_element(By.TAG_NAME, "button")
    # actions = ActionChains(driver)
    # actions.move_to_element(proceed).click().perform()
    # checkbox = driver.find_element(By.XPATH, '//*[@id="cgv"]')
    # actions = ActionChains(driver)
    # actions.move_to_element(checkbox).click().perform()
    # proceed = driver.find_element(By.NAME, "processCarrier")
    # actions = ActionChains(driver)
    # actions.move_to_element(proceed).click().perform()
    # proceed = driver.find_element(By.CLASS_NAME, "bankwire")
    # actions = ActionChains(driver)
    # actions.move_to_element(proceed).click().perform()
    # proceed = driver.find_element(By.ID, "center_column").find_element(By.TAG_NAME, "button")
    # actions = ActionChains(driver)
    # actions.move_to_element(proceed).click().perform()
    # assert driver.find_element(By.CLASS_NAME, "cheque-indent").text == "Your order on My Store is complete."
    # logging.info("bought the product successfully!")
    # driver.quit()




