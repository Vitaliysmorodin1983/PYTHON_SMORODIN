from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time


def test_sauce_demo_shopping():
    # Инициализация Firefox драйвера
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        # Открытие сайта магазина
        driver.get("https://www.saucedemo.com/")

        # Ожидание загрузки формы авторизации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )

        # Авторизация как standard_user
        username_field = driver.find_element(By.ID, "user-name")
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Ожидание загрузки каталога товаров
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        # Добавление товаров в корзину
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for product_name in products_to_add:
            add_to_cart_button = driver.find_element(
                By.XPATH,
                f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button[contains(text(), 'Add to cart')]"
            )
            add_to_cart_button.click()

        # Переход в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # Ожидание загрузки корзины
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cart_contents_container"))
        )

        # Нажатие Checkout
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Ожидание загрузки формы оформления заказа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )

        # Заполнение формы данными
        first_name_field = driver.find_element(By.ID, "first-name")
        first_name_field.send_keys("Иван")

        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Петров")

        postal_code_field = driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("123456")

        # Нажатие Continue
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        # Ожидание загрузки страницы с итоговой стоимостью
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )

        # Чтение итоговой стоимости
        total_element = driver.find_element(
            By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text

        # Проверка, что итоговая сумма равна $58.29
        assert "Total: $58.29" in total_text, f"Expected Total: $58.29, but got: {total_text}"

        print(f"Итоговая стоимость: {total_text}")

        # ЗАДЕРЖКА ТОЛЬКО НА ИТОГОВОЙ СТРАНИЦЕ - 10 СЕКУНД
        print("Итоговая страница отображается 10 секунд...")
        start_time = time.time()
        WebDriverWait(driver, 11).until(
            lambda d: time.time() - start_time > 10
        )
        print("10 секунд прошло, тест завершен")

    finally:
        # Закрытие браузера
        driver.quit()


def test_sauce_demo_alternative():
    """Альтернативная версия с задержкой только на итоговой странице"""
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Добавление товаров в корзину по ID кнопок
        add_buttons = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

        for button_id in add_buttons:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, button_id))
            ).click()

        # Переход в корзину и оформление заказа
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

        # Заполнение формы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )

        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        # Проверка итоговой стоимости
        total_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )

        total_text = total_element.text
        assert total_text == "Total: $58.29", f"Expected Total: $58.29, but got: {total_text}"

        print(f"Итоговая стоимость: {total_text}")

        # ЗАДЕРЖКА ТОЛЬКО НА ИТОГОВОЙ СТРАНИЦЕ - 10 СЕКУНД
        print("Задержка отображения итоговой страницы: 10 секунд")
        start_time = time.time()
        WebDriverWait(driver, 11).until(
            lambda d: time.time() - start_time > 10
        )
        print("Задержка завершена")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_sauce_demo_shopping()
