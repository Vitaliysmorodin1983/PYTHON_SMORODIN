from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.saucedemo.com/'

    def open(self):
        self.driver.get(self.url)
        # Ждем загрузки страницы
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, 'login-button'))
        )
        return self

    def login(self, username, password):
        # Заполняем форму логина
        username_input = self.driver.find_element(By.ID, 'user-name')
        password_input = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.ID, 'login-button')

        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        login_button.click()

        # Ждем загрузки страницы продуктов
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list'))
        )
        return ProductsPage(self.driver)


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        # Правильные ID для товаров
        product_ids = {
            'Sauce Labs Backpack': 'add-to-cart-sauce-labs-backpack',
            'Sauce Labs Bolt T-Shirt': 'add-to-cart-sauce-labs-bolt-t-shirt', 
            'Sauce Labs Onesie': 'add-to-cart-sauce-labs-onesie'
        }
        
        add_button_id = product_ids.get(product_name)
        if not add_button_id:
            raise ValueError(f"Unknown product: {product_name}")
        
        # Ждем и кликаем кнопку добавления
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, add_button_id))
        )
        add_button.click()
        
        # Небольшая пауза после добавления
        time.sleep(0.5)
        return self

    def go_to_cart(self):
        # Кликаем по иконке корзины
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))
        )
        cart_button.click()
        
        # Ждем загрузки страницы корзины
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, 'checkout'))
        )
        return CartPage(self.driver)


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'checkout'))
        )
        checkout_button.click()
        
        # Ждем загрузки формы оформления
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, 'first-name'))
        )
        return CheckoutPage(self.driver)


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_info(self, first_name, last_name, postal_code):
        # Заполняем информацию
        first_name_input = self.driver.find_element(By.ID, 'first-name')
        last_name_input = self.driver.find_element(By.ID, 'last-name')
        postal_code_input = self.driver.find_element(By.ID, 'postal-code')
        continue_button = self.driver.find_element(By.ID, 'continue')

        first_name_input.clear()
        first_name_input.send_keys(first_name)
        last_name_input.clear()
        last_name_input.send_keys(last_name)
        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)
        continue_button.click()
        
        # Ждем загрузки страницы с итогом
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'summary_info'))
        )
        return self

    def get_total_amount(self):
        total_element = self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label'
        )
        return total_element.text.split('$')[-1]