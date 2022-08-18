import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.AuthenticationPage import AuthenticationPage
from pages.CheapestProductPage import CheapestProductPage
from pages.MainPage import MainPage
from pages.MyAccountPage import MyAccountPage
from pages.SearchResultPage import SearchResultPage
from pages.ShoppingCompletePage import ShoppingCompletePage


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

