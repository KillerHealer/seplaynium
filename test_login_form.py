import logging
import time
import pytest
from playwright.sync_api import Page
from AuthenticationPage import AuthenticationPage
from MainPage import MainPage
from MyAccountPage import MyAccountPage


@pytest.fixture
def page(page: Page):
    """
    goes to the sign in page
    :param page: the page has all the elements
    :return:
    """
    page.goto("http://automationpractice.com/index.php")
    get_started = MainPage(page)
    return get_started.SignIn()


def test_login_form_logged_in(page):
    """
    tries to login with normal credentials and check if the page has swapped
    :param page: the page has all the elements
    :return:
    """
    authentication_page = AuthenticationPage(page)
    my_account_page = MyAccountPage(authentication_page.login("noam@gmail.com", "Abcd1234@"))
    logging.info("trying to login with normal and correct credentials!")
    time.sleep(3)
    assert my_account_page.current_url() == "http://automationpractice.com/index.php?controller=my-account"
    assert my_account_page.get_account_name() == "noam noam"
    time.sleep(3)
    my_account_page.quit()


def test_login_form_logged_in_failed(page):
    """
    tries to input wrong credentials and to find the specific error warning "Authentication failed."
    :param page: the page has all the elements
    :return:
    """
    authentication_page = AuthenticationPage(page)
    my_account_page = MyAccountPage(authentication_page.login("noam@gmail.com", "Abcd14@"))
    logging.info("trying to login with incorrect credentials!")
    time.sleep(3)
    assert my_account_page.find_error() == "Authentication failed."
    time.sleep(3)
    my_account_page.quit()


def test_login_form_without_password_failed(page):
    """
    tries to input wrong credentials and to find the specific error warning "Password is required."
    :param page: the page has all the elements
    :return:
    """
    authentication_page = AuthenticationPage(page)
    my_account_page = MyAccountPage(authentication_page.login("noam@gmail.com", ""))
    logging.info("trying to login without the password!")
    time.sleep(3)
    assert my_account_page.find_error() == "Password is required."
    time.sleep(3)
    my_account_page.quit()


def test_login_form_without_email_failed(page):
    """
    tries to input wrong credentials and to find the specific error warning "An email address required."
    :param page: the page has all the elements
    :return:
    """
    authentication_page = AuthenticationPage(page)
    my_account_page = MyAccountPage(authentication_page.login("", "Abcd1234@"))
    logging.info("trying to login without the email!")
    time.sleep(3)
    assert my_account_page.find_error() == "An email address required."
    time.sleep(3)
    my_account_page.quit()


def test_click_forgot_password(page):
    """
    tries to click to the 'Forgot your password?' button
    :param page: the page has all the elements
    :return:
    """
    authentication_page = AuthenticationPage(page)
    logging.info("trying to go to the forgot password page!")
    my_account_page = MyAccountPage(authentication_page.forgot_password())
    time.sleep(3)
    assert my_account_page.current_url() == "http://automationpractice.com/index.php?controller=password"
    time.sleep(3)
    my_account_page.quit()

