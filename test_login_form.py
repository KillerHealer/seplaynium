import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrom_driver_path = "D:\pythonProject\chromedriver.exe"


def get_to_login_page():
    """
    gets page to login page
    :return:
    """
    logging.info("going from the home page to the sign in page!")
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php')
    login_btn = driver.find_element(By.CLASS_NAME, "login")
    login_btn.click()
    time.sleep(3)
    return driver


def test_login_form_logged_in():
    """
    tries to login with normal credentials and check if the page has swapped
    :return:
    """
    driver = get_to_login_page()
    login_form = driver.find_element(By.XPATH, '//*[@id="login_form"]')
    email_input = login_form.find_element(By.XPATH, '//*[@id="email"]')
    email_input.send_keys("noam@gmail.com")
    pass_input = login_form.find_element(By.XPATH, '//*[@id="passwd"]')
    pass_input.send_keys("Abcd1234@")
    sign_in_btn = login_form.find_element(By.XPATH, '//*[@id="SubmitLogin"]')
    sign_in_btn.click()
    logging.info("trying to login with normal and correct credentials!")
    time.sleep(3)
    assert driver.current_url == "http://automationpractice.com/index.php?controller=my-account"
    assert driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span').text == "noam noam"
    time.sleep(3)
    driver.quit()


def test_login_form_logged_in_failed():
    """
    tries to input wrong credentials and to find the specific error warning "Authentication failed."
    :return:
    """
    driver = get_to_login_page()
    login_form = driver.find_element(By.XPATH, '//*[@id="login_form"]')
    email_input = login_form.find_element(By.XPATH, '//*[@id="email"]')
    email_input.send_keys("noam@gmail.com")
    pass_input = login_form.find_element(By.XPATH, '//*[@id="passwd"]')
    pass_input.send_keys("Abcd14@")
    sign_in_btn = login_form.find_element(By.XPATH, '//*[@id="SubmitLogin"]')
    sign_in_btn.click()
    logging.info("trying to login with incorrect credentials!")
    time.sleep(3)
    assert driver.find_element(By.XPATH, '//*[@id="center_column"]/div[1]') \
        .find_element(By.XPATH, '//*[@id="center_column"]/div[1]/ol/li').text == "Authentication failed."
    time.sleep(3)
    driver.quit()


def test_login_form_without_password_failed():
    """
    tries to input wrong credentials and to find the specific error warning "Password is required."
    :return:
    """
    driver = get_to_login_page()
    login_form = driver.find_element(By.XPATH, '//*[@id="login_form"]')
    email_input = login_form.find_element(By.XPATH, '//*[@id="email"]')
    email_input.send_keys("noam@gmail.com")
    sign_in_btn = login_form.find_element(By.XPATH, '//*[@id="SubmitLogin"]')
    sign_in_btn.click()
    logging.info("trying to login without the password!")
    time.sleep(3)
    assert driver.find_element(By.XPATH, '//*[@id="center_column"]/div[1]') \
        .find_element(By.XPATH, '//*[@id="center_column"]/div[1]/ol/li').text == "Password is required."
    time.sleep(3)
    driver.quit()


def test_login_form_without_email_failed():
    """
    tries to input wrong credentials and to find the specific error warning "An email address required."
    :return:
    """
    driver = get_to_login_page()
    login_form = driver.find_element(By.XPATH, '//*[@id="login_form"]')
    pass_input = login_form.find_element(By.XPATH, '//*[@id="passwd"]')
    pass_input.send_keys("Abcd1234@")
    sign_in_btn = login_form.find_element(By.XPATH, '//*[@id="SubmitLogin"]')
    sign_in_btn.click()
    logging.info("trying to login without the email!")
    time.sleep(3)
    assert driver.find_element(By.XPATH, '//*[@id="center_column"]/div[1]') \
        .find_element(By.XPATH, '//*[@id="center_column"]/div[1]/ol/li').text == "An email address required."
    time.sleep(3)
    driver.quit()


def test_forgot_password_btn():
    driver = get_to_login_page()
    logging.info("trying to go to the forgot password page!")
    driver.find_element(By.XPATH, '//a[text()="Forgot your password?"]').click()
    time.sleep(3)
    assert driver.current_url == "http://automationpractice.com/index.php?controller=password"
    time.sleep(3)
    driver.quit()
