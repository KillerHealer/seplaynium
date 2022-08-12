import logging
import re
import time

from playwright.sync_api import Page, expect


def test_buy_cheapest_dress(page: Page):
    """
    tries to find the cheapest dress from the search for summer and buys it
    :return:
    """
    page.goto("http://automationpractice.com/index.php")
    expect(page).to_have_title(re.compile("My Store"))
    get_started = page.locator('xpath=//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
    expect(get_started).to_have_attribute("href", "http://automationpractice.com/index.php?controller=my-account")
    get_started.click()
    logging.info("going from the home screen to the login screen!")
    expect(page).to_have_url(re.compile(".*my-account"))
    email_input = page.locator("id=email")
    email_input.type("noam@gmail.com")
    pass_input = page.locator("id=passwd")
    pass_input.type("Abcd1234@")
    sign_in_btn = page.locator("id=SubmitLogin")
    sign_in_btn.click()
    logging.info("signing in!")
    expect(page).to_have_url(re.compile(".*my-account"))
    search_box = page.locator("id=search_query_top")
    search_btn = page.locator("button.button-search")
    search_box.type("summer")
    search_btn.click()
    logging.info("searching for the word 'summer' in the search bar and going to the search page!")
    time.sleep(4)
    expect(page).to_have_url("http://automationpractice.com/"
                             "index.php?controller=search&orderby=position&orderway=desc&search_query=summer"
                             "&submit_search=")
    products_list = page.locator('ul.product_list li')
    prices = page.locator("ul.product_list li .product-price")
    prices_list = []
    for price in prices.all_inner_texts():
        prices_list.append(re.sub('[^\d\.]', "", price))
    cheapest_product = products_list.locator(f".product-container:has-text('${(min(prices_list))}')")
    cheapest_product.hover()
    logging.info("finding the cheapest product in the search page and starting to buy it!")
    page.wait_for_timeout(3000)
    cheapest_product.locator("text='Add to cart'").click()
    time.sleep(5)
    page.locator("text='Proceed to checkout'").click()
    time.sleep(2)
    page.locator("#center_column >> text='Proceed to checkout'").click()
    page.locator("button >> text='Proceed to checkout'").click()
    checkbox = page.locator("input#cgv")
    checkbox.click()
    page.locator("button >> text='Proceed to checkout'").click()
    page.locator("text='Pay by bank wire'").click()
    page.locator("button >> text='I confirm my order'").click()
    assert "Your order on My Store is complete" in page.locator('body').inner_html()
    logging.info("bought the product successfully!")
