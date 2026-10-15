class CheckoutPage:

    def __init__(self, page):
        self.page = page
        self._first_name = page.get_by_placeholder("First Name")
        self._last_name = page.get_by_placeholder("Last Name")
        self._zip_postal_code = page.get_by_placeholder("Zip/Postal Code")
        self._continue_button = page.locator("#continue")
        self._finish_button = page.locator("#finish")
        self._confirm_header_msg = page.locator("h2.complete-header")

    def enter_first_name(self, f_name):
        self._first_name.fill(f_name)
        return self

    def enter_last_name(self, l_name):
        self._last_name.fill(l_name)
        return self

    def enter_poatal_code(self, p_code):
        self._zip_postal_code.fill(p_code)
        return self

    def enter_checkout_details(self, f_name, l_name, p_code):
        self.enter_first_name(f_name).enter_last_name(l_name).enter_poatal_code(p_code)
        return self

    def click_on_continue_button(self):
        self._continue_button.click()
        return self
        
    def click_finish_button(self):
        self._finish_button.click()
        return self
        
    def get_confirmation_message_for_order_purchase(self):
        return self._confirm_header_msg
