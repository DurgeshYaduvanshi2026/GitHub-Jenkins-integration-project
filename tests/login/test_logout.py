from playwright.sync_api import Page, expect

import pytest
from config import Config
from src.pages.LoginPage import LoginPage


@pytest.mark.sanity
def test_logout(page: Page) -> None:

    login_page = LoginPage(page)
    products_page = login_page.do_login(
        {
            "username": Config.email,
            "password": Config.password,
        }
    )
    products_page.do_logout()
    expect(login_page.verify_login_page()).to_be_visible()
