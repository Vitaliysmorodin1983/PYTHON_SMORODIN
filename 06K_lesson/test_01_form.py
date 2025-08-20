from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_form_validation_edge():
    # Ручная настройка Edge драйвера
    service = EdgeService(
        r"C:\Users\smoro\Downloads\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service)

    try:
        # Открытие страницы
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Ожидание загрузки формы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )

        # Заполнение полей формы
        fields_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for field_name, value in fields_data.items():
            field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, field_name))
            )
            field.clear()
            field.send_keys(value)

        # Zip code оставляем пустым

        # Нажатие кнопки Submit
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()

        # Ожидание применения стилей валидации
        WebDriverWait(driver, 10).until(
            lambda d: "alert-danger" in d.find_element(
                By.NAME, "zip-code").get_attribute("class")
        )

        # Проверка, что поле Zip code подсвечено красным
        zip_code_field = driver.find_element(By.NAME, "zip-code")
        zip_code_classes = zip_code_field.get_attribute("class")
        assert "alert-danger" in zip_code_classes, "Zip code field should be highlighted red"

        # Проверка, что остальные поля подсвечены зеленым
        fields_to_check = list(fields_data.keys())

        for field_name in fields_to_check:
            field = driver.find_element(By.NAME, field_name)
            field_classes = field.get_attribute("class")
            assert "alert-success" in field_classes, f"Field {field_name} should be highlighted green"

        # Ожидание 10 секунд с заполненной формой (без sleep!)
        print("Форма заполнена и проверена. Ожидание 10 секунд...")

        # Создаем кастомное ожидание на 10 секунд
        start_time = time.time()
        WebDriverWait(driver, 11).until(
            lambda d: time.time() - start_time > 10
        )

        print("10 секунд прошло, тест завершен")

    finally:
        # Закрытие браузера
        driver.quit()


# Альтернативная версия с Chrome
def test_form_validation_chrome():
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )

        fields_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for field_name, value in fields_data.items():
            field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, field_name))
            )
            field.clear()
            field.send_keys(value)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()

        WebDriverWait(driver, 10).until(
            lambda d: "alert-danger" in d.find_element(
                By.NAME, "zip-code").get_attribute("class")
        )

        zip_code_field = driver.find_element(By.NAME, "zip-code")
        assert "alert-danger" in zip_code_field.get_attribute("class")

        for field_name in fields_data.keys():
            field = driver.find_element(By.NAME, field_name)
            assert "alert-success" in field.get_attribute("class")

        # Ожидание 10 секунд
        print("Форма заполнена и проверена. Ожидание 10 секунд...")
        start_time = time.time()
        WebDriverWait(driver, 11).until(
            lambda d: time.time() - start_time > 10
        )
        print("10 секунд прошло, тест завершен")

    finally:
        driver.quit()


if __name__ == "__main__":
    # Попробуем сначала Chrome
    try:
        test_form_validation_chrome()
        print("Chrome test passed!")
    except Exception as e:
        print(f"Chrome test failed: {e}")
        # Если Chrome не работает, попробуем Edge
        test_form_validation_edge()
