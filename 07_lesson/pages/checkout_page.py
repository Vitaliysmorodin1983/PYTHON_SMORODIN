from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_input = (By.ID, 'first-name')
        self.last_name_input = (By.ID, 'last-name')
        self.postal_code_input = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.total_label = (By.CLASS_NAME, 'summary_total_label')

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.wait_for_element(self.first_name_input).send_keys(first_name)
        self.wait_for_element(self.last_name_input).send_keys(last_name)
        self.wait_for_element(self.postal_code_input).send_keys(postal_code)
        self.wait_for_element_clickable(self.continue_button).click()
        return self

    def get_total_amount(self):
        total_element = self.wait_for_element(self.total_label)
        return total_element.text.split('$')[-1]