import logging
import re
import time
from playwright.sync_api import Page, expect
from pages.BasicPage import BasicPage


class AuthenticationPage(BasicPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._locators = {"email_locate": "id=email",
                          "password_locate": "id=passwd",
                          "login_btn_locate": "id=SubmitLogin",
                          "forgot_password": "text=Forgot your password?"}

    def login(self, username: str, password: str):
        login_form = self._page.locator(*self._locators["login_form"])
        login_form.locator(*self._locators["email_locate"]).type(username)
        login_form.locator(*self._locators["password_locate"]).type(password)
        login_form.locator(*self._locators["login_btn_locate"]).click()
        return self._page

    def forgot_password(self):
        self._page.locator(self._locators["forgot_password"]).click()

