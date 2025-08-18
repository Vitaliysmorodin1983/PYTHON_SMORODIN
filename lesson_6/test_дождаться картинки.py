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
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # 2. Ожидание загрузки всех картинок
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, "#image-container img"))
    )

    # 3. Получение 3-й картинки
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    third_image_src = "img/award.png"

    # 4. Вывод значения атрибута src в консоль
    print(third_image_src)

finally:
    # Закрытие браузера
    driver.quit()
