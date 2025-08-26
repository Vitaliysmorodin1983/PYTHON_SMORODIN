from selenium.webdriver.common.by import By
from .base_page import BasePage
from .cart_page import CartPage


class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.inventory_list = (By.CLASS_NAME, 'inventory_list')

    def add_products_to_cart(self):
        products_to_add = [
            'sauce-labs-backpack',
            'sauce-labs-bolt-t-shirt',
            'sauce-labs-onesie'
        ]
        
        for product_id in products_to_add:
            add_button = (By.ID, f'add-to-cart-{product_id}')
            self.wait_for_element_clickable(add_button).click()
        
        return self

    def go_to_cart(self):
        cart_button = (By.CLASS_NAME, 'shopping_cart_link')
        self.wait_for_element_clickable(cart_button).click()
        return CartPage(self.driver)