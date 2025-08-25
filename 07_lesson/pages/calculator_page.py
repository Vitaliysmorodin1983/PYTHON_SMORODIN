from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            'https://bonigarcia.dev/selenium-webdriver-java/'
            'slow-calculator.html'
        )

    def open(self):
        self.driver.get(self.url)
        # Исправленный локатор - ждем любой элемент калькулятора
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        return self

    def set_delay(self, delay):
        delay_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#delay'))
        )
        delay_input.clear()
        delay_input.send_keys(str(delay))
        return self

    def click_button(self, button_text):
        button_locator = (By.XPATH, f'//span[text()="{button_text}"]')
        
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        
        self.driver.execute_script("arguments[0].click();", button)
        return self

    def get_result(self):
        try:
            result_element = self.driver.find_element(By.CSS_SELECTOR, '.screen')
            return result_element.text.strip()
        except:
            return ""