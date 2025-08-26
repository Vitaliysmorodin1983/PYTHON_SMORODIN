from selenium.webdriver.common.by import By
from .base_page import BasePage
from .checkout_page import CheckoutPage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_list = (By.CLASS_NAME, 'cart_list')
        self.checkout_button = (By.ID, 'checkout')

    def checkout(self):
        self.wait_for_element_clickable(self.checkout_button).click()
        return CheckoutPage(self.driver)