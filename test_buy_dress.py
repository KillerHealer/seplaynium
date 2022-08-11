import re
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
    expect(page).to_have_url(re.compile(".*my-account"))
    email_input = page.locator("id=email")
    email_input.type("noam@gmail.com")
    pass_input = page.locator("id=passwd")
    pass_input.type("Abcd1234@")
    sign_in_btn = page.locator("id=SubmitLogin")
    sign_in_btn.click()
    expect(page).to_have_url(re.compile(".*my-account"))
