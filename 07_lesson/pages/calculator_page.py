from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
        self.delay_input = (By.CSS_SELECTOR, '#delay')
        self.screen = (By.CSS_SELECTOR, '.screen')
        self.wait = WebDriverWait(driver, timeout=50)

    def open(self):
        self.driver.get(self.url)
        return self

    def set_delay(self, delay):
        delay_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delay_input)
        )
        delay_element.clear()
        delay_element.send_keys(str(delay))
        return self

    def click_button(self, button_text):
        button_locator = (By.XPATH, f'//span[text()="{button_text}"]')
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()
        return self

    def perform_calculation(self):
        self.click_button('7')
        self.click_button('+')
        self.click_button('8')
        self.click_button('=')
        return self

    def get_result(self):
        result_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.screen)
        )
        return result_element.text

    def wait_for_result(self, expected_result):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(self.screen, expected_result)
        )
        return self.get_result()