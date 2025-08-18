from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService

# Настройка Edge WebDriver
service = EdgeService(
    r"C:\Users\smoro\Downloads\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)

try:
    # 1. Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # 2. Нажатие на синюю кнопку
    ajax_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
    ajax_button.click()

    # 3. Ожидание появления зеленой плашки с явным ожиданием
    green_banner = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )

    # 4. Вывод текста в консоль
    print(green_banner.text)  # "Data loaded with AJAX get request."

finally:
    # Закрытие браузера
    driver.quit()
