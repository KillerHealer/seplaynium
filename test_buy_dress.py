import logging
import re
import time
import pytest
from playwright.sync_api import Page, expect
from AuthenticationPage import AuthenticationPage
from CheapestProductPage import CheapestProductPage
from MainPage import MainPage
from MyAccountPage import MyAccountPage
from SearchResultPage import SearchResultPage
from ShoppingCompletePage import ShoppingCompletePage


@pytest.fixture
def page(page: Page):
    page.goto("http://automationpractice.com/index.php")
    expect(page).to_have_title(re.compile("My Store"))
    get_started = MainPage(page)
    return get_started.SignIn()


def test_buy_cheapest_dress(page):
    """
    tries to find the cheapest dress from the search for summer and buys it
    :return:
    """
    authentication_page = AuthenticationPage(page)
    my_account_page = MyAccountPage(authentication_page.login("noam@gmail.com", "Abcd1234@"))
    main_page = MainPage(my_account_page.home())
    time.sleep(3)
    search_result_page = SearchResultPage(main_page.search("summer"))
    time.sleep(3)
    cheapest_product_page = CheapestProductPage(search_result_page.find_cheapest())
    time.sleep(3)
    shopping_complete_page = ShoppingCompletePage(cheapest_product_page.buy())
    time.sleep(3)
    assert shopping_complete_page.success()
    logging.info("bought the product successfully!")
    shopping_complete_page._page.close()
