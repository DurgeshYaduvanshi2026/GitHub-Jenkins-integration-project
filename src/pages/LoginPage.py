import pytest
from playwright.sync_api import Page, expect
from .ProductListPage import ProductListPage


class LoginPage:

    # Constructor

    def __init__(self, page: Page):
        self.page = page
        self._usernameid = page.get_by_placeholder("Username")
        self._passwordid = page.get_by_placeholder("Password")
        self._login_button = page.get_by_text("Login")

        self._error_message_wrong_email_id = page.locator('[data-test="error"]')

    def enter_username(self, u_name):
        self._usernameid.clear()
        self._usernameid.fill(u_name)

    def enter_password(self, u_pass):
        self._passwordid.clear()
        self._passwordid.fill(u_pass)

    def click_on_login_button(self):
        self._login_button.click()

    def verify_login_page(self):
        return self._login_button

    def error_msg_verify(self):
        return self._error_message_wrong_email_id

    def error_msg_without_email_and_password(self):
        return self._error_message_wrong_email_id

    def login(self, username: str, password: str) -> None:
        """Submit the login form with the supplied credentials."""
        self._usernameid.fill(username)
        self._passwordid.fill(password)
        self._login_button.click()

    def do_login(self, credentials: dict[str, str]) -> ProductListPage:
        self.enter_username(credentials["username"])
        self.enter_password(credentials["password"])
        self.click_on_login_button()

        return ProductListPage(self.page)
