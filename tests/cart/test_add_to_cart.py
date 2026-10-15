import pytest
from playwright.sync_api import Page, expect

from config import Config
from src.pages.LoginPage import LoginPage


def test_add_to_cart(page: Page) -> None:
    login_page = LoginPage(page)

    products_page = login_page.do_login(
        {
            "username": Config.email,
            "password": Config.password,
        }
    )

    product_name = "Sauce Labs Onesie"
    products_page.click_add_to_cart_or_remove(product_name)
    expect(products_page.get_add_remove_cart_locators(product_name)).to_have_text(
        "Remove"
    )


def test_remove_product_from_cart(page: Page) -> None:
    login_page = LoginPage(page)

    products_page = login_page.do_login(
        {
            "username": Config.email,
            "password": Config.password,
        }
    )

    product_name = "Sauce Labs Onesie"
    products_page.click_add_to_cart_or_remove(product_name)
    products_page.click_add_to_cart_or_remove(product_name)
    expect(products_page.get_add_remove_cart_locators(product_name)).to_have_text(
        "Add to cart"
    )
