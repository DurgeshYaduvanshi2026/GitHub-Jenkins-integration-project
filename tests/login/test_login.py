import pytest
from playwright.sync_api import Page, expect

from config import Config
from src.pages.LoginPage import LoginPage


@pytest.mark.sanity
def test_login_with_standard_user(page: Page) -> None:
    login_page = LoginPage(page)

    products_page = login_page.do_login(
        {
            "username": Config.email,
            "password": Config.password,
        }
    )

    expect(products_page.product_header).to_be_visible()


@pytest.mark.sanity
def test_invalid_login(page: Page) -> None:
    login_page = LoginPage(page)

    login_page.do_login(
        {
            "username": Config.invalid_email,
            "password": Config.invalid_password,
        }
    )

    expected_error_message = (
        "Epic sadface: Username and password do not match any user in this service"
    )

    expect(login_page.error_msg_verify()).to_contain_text(expected_error_message)
    
    
def test_login_with_no_credentials(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.do_login(
        {
            "username": "",
            "password": "",
        }
    )

    expected_failed_message = "Username is required"
    expect(login_page.error_msg_without_email_and_password()).to_contain_text(
        expected_failed_message
    )
