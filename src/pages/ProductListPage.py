from .CartPage import CartPage


class ProductListPage:

    def __init__(self, page):
        self.page = page
        self._product_header_home_page = page.locator("span.title")
        self._burger_menu = page.locator("#react-burger-menu-btn")
        self._logout_btn = page.locator("#logout_sidebar_link")

        self._cart_icon = page.locator("a.shopping_cart_link")

    @property
    def product_header(self):
        """_summary_

        Returns:
            _type_: it return locator or selector for product header text
        """
        return self._product_header_home_page

    def click_hamburger_menu(self):
        """_this will click on burger menu icon from header_"""
        self._burger_menu.click()

    def click_logout_btn(self):
        self._logout_btn.click()

    def do_logout(self):
        self.click_hamburger_menu()
        self.click_logout_btn()

    def get_add_remove_cart_locators(self, product):
        """Return the Add to cart or Remove button for a product."""
        product_slug = product.lower().replace(" ", "-")
        return self.page.locator(f'[data-test$="{product_slug}"]')

    def click_add_to_cart_or_remove(self, product):
        self.get_add_remove_cart_locators(product).click()
        return self
        
        
    def click_cart_icon(self):
        self._cart_icon.click()
        return CartPage(self.page)
