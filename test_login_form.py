import re
from playwright.sync_api import Page, expect


def get_to_sign_in_page(page: Page):
    """
    goes to the sign in page
    :param page: the page has all the elements
    :return:
    """
    page.goto("http://automationpractice.com/index.php")
    expect(page).to_have_title(re.compile("My Store"))
    get_started = page.locator('xpath=//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
    expect(get_started).to_have_attribute("href", "http://automationpractice.com/index.php?controller=my-account")
    get_started.click()
    expect(page).to_have_url(re.compile(".*my-account"))


def test_login_form_logged_in(page: Page):
    """
    tries to login with normal credentials and check if the page has swapped
    :param page: the page has all the elements
    :return:
    """
    get_to_sign_in_page(page)
    email_input = page.locator("id=email")
    email_input.type("noam@gmail.com")
    pass_input = page.locator("id=passwd")
    pass_input.type("Abcd1234@")
    sign_in_btn = page.locator("id=SubmitLogin")
    sign_in_btn.click()
    expect(page).to_have_url(re.compile(".*my-account"))
    assert page.locator('xpath=//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span').text_content() == "noam noam"


def test_login_form_logged_in_failed(page:Page):
    """
    tries to input wrong credentials and to find the specific error warning "Authentication failed."
    :param page: the page has all the elements
    :return:
    """
    get_to_sign_in_page(page)
    email_input = page.locator("id=email")
    email_input.type("noam@gmail.com")
    pass_input = page.locator("id=passwd")
    pass_input.type("Abcd134@")
    sign_in_btn = page.locator("id=SubmitLogin")
    sign_in_btn.click()
    expect(page).to_have_url(re.compile(".*authentication"))
    assert page.locator("text=Authentication failed.").text_content() == 'Authentication failed.'


def test_login_form_without_password_failed(page: Page):
    """
    tries to input wrong credentials and to find the specific error warning "Password is required."
    :param page: the page has all the elements
    :return:
    """
    get_to_sign_in_page(page)
    email_input = page.locator("id=email")
    email_input.type("noam@gmail.com")
    sign_in_btn = page.locator("id=SubmitLogin")
    sign_in_btn.click()
    expect(page).to_have_url(re.compile(".*authentication"))
    assert page.locator("text=Password is required.").text_content() == "Password is required."


def test_login_form_without_email_failed(page: Page):
    """
    tries to input wrong credentials and to find the specific error warning "An email address required."
    :param page: the page has all the elements
    :return:
    """
    get_to_sign_in_page(page)
    pass_input = page.locator("id=passwd")
    pass_input.type("Abcd134@")
    sign_in_btn = page.locator("id=SubmitLogin")
    sign_in_btn.click()
    expect(page).to_have_url(re.compile(".*authentication"))
    assert page.locator("text=An email address required.").text_content() == "An email address required."


def test_click_forgot_password(page: Page):
    """
    tries to click to the 'Forgot your password?' button
    :param page: the page has all the elements
    :return:
    """
    get_to_sign_in_page(page)
    page.locator("text=Forgot your password?").click()
    assert page.url == "http://automationpractice.com/index.php?controller=password"


