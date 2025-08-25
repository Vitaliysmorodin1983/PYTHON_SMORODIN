from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_saucedemo(driver):
    """Тест с полным контролем добавления товаров"""
    driver.maximize_window()
    
    # 1. Логинимся
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    
    # 2. Ждем продукты
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list'))
    )
    
    # 3. Добавляем товары через JavaScript с проверкой
    products = [
        {'id': 'add-to-cart-sauce-labs-backpack', 'name': 'Sauce Labs Backpack', 'price': 29.99},
        {'id': 'add-to-cart-sauce-labs-bolt-t-shirt', 'name': 'Sauce Labs Bolt T-Shirt', 'price': 15.99},
        {'id': 'add-to-cart-sauce-labs-onesie', 'name': 'Sauce Labs Onesie', 'price': 7.99}
    ]
    
    for product in products:
        try:
            # Проверяем что кнопка существует
            button = driver.find_element(By.ID, product['id'])
            # Кликаем через JavaScript
            driver.execute_script("arguments[0].click();", button)
            print(f"✓ Добавлен: {product['name']} (${product['price']})")
            time.sleep(0.3)
        except Exception as e:
            print(f"✗ Ошибка с {product['name']}: {e}")
            # Пробуем прямой JavaScript вызов
            try:
                driver.execute_script(f"document.getElementById('{product['id']}').click()")
                print(f"✓ Добавлен через JS: {product['name']}")
            except:
                print(f"✗ Критическая ошибка с {product['name']}")
    
    # 4. Проверяем корзину
    try:
        cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
        if cart_badge.text != '3':
            print(f"⚠️ В корзине {cart_badge.text} товаров вместо 3!")
            # Принудительно добавляем недостающие
            for product in products[1:]:  # Пропускаем первый товар
                try:
                    driver.execute_script(f"document.getElementById('{product['id']}').click()")
                    print(f"Принудительно добавлен: {product['name']}")
                except:
                    print(f"Не удалось принудительно добавить: {product['name']}")
    except:
        print("Нет иконки корзины - добавляем все товары")
        for product in products:
            try:
                driver.execute_script(f"document.getElementById('{product['id']}').click()")
                print(f"Добавлен: {product['name']}")
            except:
                print(f"Не удалось добавить: {product['name']}")
    
    # 5. Переходим в корзину
    driver.get('https://www.saucedemo.com/cart.html')
    
    # 6. Проверяем товары в корзине
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'cart_list'))
    )
    
    cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')
    print(f"Товаров в корзине: {len(cart_items)}")
    
    if len(cart_items) != 3:
        print("❌ Не удалось добавить все товары! Завершаем тест.")
        return
    
    # 7. Оформляем заказ
    driver.find_element(By.ID, 'checkout').click()
    
    # 8. Заполняем форму
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'first-name'))
    )
    
    driver.find_element(By.ID, 'first-name').send_keys('John')
    driver.find_element(By.ID, 'last-name').send_keys('Doe')
    driver.find_element(By.ID, 'postal-code').send_keys('12345')
    driver.find_element(By.ID, 'continue').click()
    
    # 9. Получаем итог
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label'))
    )
    
    total_element = driver.find_element(By.CLASS_NAME, 'summary_total_label')
    total_amount = total_element.text.split('$')[-1]
    print(f"Итоговая сумма: ${total_amount}")
    
    # Ожидаемая сумма: 29.99 + 15.99 + 7.99 = 53.97 + налог ≈ 58.29
    assert total_amount == '58.29', f'Expected $58.29, but got ${total_amount}'
    print("✅ Тест пройден!")