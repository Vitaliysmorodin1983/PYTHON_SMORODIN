from selenium.webdriver.common.by import By
from .base_page import BasePage
from .products_page import ProductsPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.saucedemo.com/'
        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def open(self):
        self.driver.get(self.url)
        return self

    def login(self, username, password):
        self.wait_for_element(self.username_input).send_keys(username)
        self.wait_for_element(self.password_input).send_keys(password)
        self.wait_for_element_clickable(self.login_button).click()
        return ProductsPage(self.driver)