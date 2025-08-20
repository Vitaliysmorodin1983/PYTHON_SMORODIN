from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_slow_calculator():
    # Инициализация Chrome драйвера
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Открытие страницы
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Ожидание загрузки калькулятора
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "delay"))
        )

        # Ввод значения задержки 45 секунд
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажатие кнопок: 7 + 8 =
        seven_button = driver.find_element(By.XPATH, "//span[text()='7']")
        seven_button.click()

        plus_button = driver.find_element(By.XPATH, "//span[text()='+']")
        plus_button.click()

        eight_button = driver.find_element(By.XPATH, "//span[text()='8']")
        eight_button.click()

        equals_button = driver.find_element(By.XPATH, "//span[text()='=']")
        equals_button.click()

        # Ожидание появления результата в течение 46 секунд (45 + запас)
        result_element = WebDriverWait(driver, 46).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        # Проверка результата
        screen = driver.find_element(By.CLASS_NAME, "screen")
        assert screen.text == "15", f"Expected result: 15, but got: {
            screen.text}"

        print("Тест успешно завершен! Результат: 15")

    finally:
        # Закрытие браузера
        driver.quit()


def test_slow_calculator_with_progress():
    """Версия с выводом прогресса ожидания"""
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "delay"))
        )

        # Установка задержки
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Ввод выражения 7 + 8
        buttons_to_click = ["7", "+", "8", "="]

        for button_text in buttons_to_click:
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//span[text()='{button_text}']"))
            )
            button.click()

        # Ожидание результата с прогрессом
        print("Ожидание результата в течение 45 секунд...")

        # Ждем пока экран перестанет быть пустым (начало вычислений)
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "")
        )

        # Ждем окончания вычислений (появление результата 15)
        screen = driver.find_element(By.CLASS_NAME, "screen")

        result = WebDriverWait(driver, 46).until(
            lambda d: screen.text if screen.text == "15" else False
        )

        assert result == "15", f"Expected result: 15, but got: {result}"
        print("Результат получен: 15")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()
