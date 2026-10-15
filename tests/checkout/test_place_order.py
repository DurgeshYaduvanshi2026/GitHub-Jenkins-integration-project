import pytest
from playwright.sync_api import Page, expect

from config import Config
from src.pages.LoginPage import LoginPage


def test_place_order(page: Page) -> None:
    login_page = LoginPage(page)

    products_page = login_page.do_login(
        {
            "username": Config.email,
            "password": Config.password,
        }
    )

    product_name = "Sauce Labs Fleece Jacket"
    checkout_page = (
        products_page.click_add_to_cart_or_remove(product_name)
        .click_cart_icon()
        .click_on_checkout_button()
        .enter_checkout_details("t1", "r4", "2334")
        .click_on_continue_button()
        .click_finish_button()
    )

    expect(checkout_page.get_confirmation_message_for_order_purchase()).to_have_text(
        "Thank you for your order!"
    )
