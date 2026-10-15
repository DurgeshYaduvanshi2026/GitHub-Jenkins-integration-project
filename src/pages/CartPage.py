from .CheckoutPage import CheckoutPage


class CartPage:

    def __init__(self, page):
        self.page = page
        self._checkout_button = page.locator("#checkout")

    def click_on_checkout_button(self):
        self._checkout_button.click()
        return CheckoutPage(self.page)
