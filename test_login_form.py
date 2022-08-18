import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.AuthenticationPage import AuthenticationPage
from pages.MainPage import MainPage
from pages.MyAccountPage import MyAccountPage


@pytest.fixture()
def main_page():
    """
    gets page to login page
    :return:
    """
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrom_driver_path = "D:\pythonProject\chromedriver.exe"
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get("http://automationpractice.com/index.php")
    main_page = MainPage(driver)
    return main_page


def test_login_form_logged_in(main_page):
    """
    tries to login with normal credentials and check if the page has swapped
    :return:
    """
    authentication_page = AuthenticationPage(main_page.SignIn())
    my_account_page = MyAccountPage(authentication_page.login("noam@gmail.com", "Abcd1234@"))
    logging.info("trying to login with normal and correct credentials!")
    time.sleep(3)
    assert my_account_page.current_url() == "http://automationpractice.com/index.php?controller=my-account"
    assert my_account_page.get_account_name() == "noam noam"
    time.sleep(3)
    my_account_page.quit()


def test_login_form_logged_in_failed(main_page):
    """
    tries to input wrong credentials and to find the specific error warning "Authentication failed."
    :return:
    """
    authentication_page = AuthenticationPage(main_page.SignIn())
    my_account_page = MyAccountPage(authentication_page.login("noam@gmail.com", "Abcd14@"))
    logging.info("trying to login with incorrect credentials!")
    time.sleep(3)
    assert my_account_page.find_error() == "Authentication failed."
    time.sleep(3)
    my_account_page.quit()


def test_login_form_without_password_failed():
    """
    tries to input wrong credentials and to find the specific error warning "Password is required."
    :return:
    """
    authentication_page = AuthenticationPage(main_page.SignIn())
    my_account_page = MyAccountPage(authentication_page.login("noam@gmail.com", ""))
    logging.info("trying to login without the password!")
    time.sleep(3)
    assert my_account_page.find_error() == "Password is required."
    time.sleep(3)
    my_account_page.quit()


def test_login_form_without_email_failed(main_page):
    """
    tries to input wrong credentials and to find the specific error warning "An email address required."
    :return:
    """
    authentication_page = AuthenticationPage(main_page.SignIn())
    my_account_page = MyAccountPage(authentication_page.login("", "Abcd1234@"))
    logging.info("trying to login without the email!")
    time.sleep(3)
    assert my_account_page.find_error() == "An email address required."
    time.sleep(3)
    my_account_page.quit()


def test_forgot_password_btn(main_page):
    """
    tries to goes to forgot password page
    :return:
    """
    authentication_page = AuthenticationPage(main_page.SignIn())
    logging.info("trying to go to the forgot password page!")
    my_account_page = MyAccountPage(authentication_page.forgot_password())
    time.sleep(3)
    assert my_account_page.current_url() == "http://automationpractice.com/index.php?controller=password"
    time.sleep(3)
    my_account_page.quit()
