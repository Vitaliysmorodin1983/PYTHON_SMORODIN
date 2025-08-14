from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_and_get_message():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    try:

        driver.get("http://the-internet.herokuapp.com/login")

        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")

        login_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        message_text = success_message.text.strip()
        print("Сообщение системы:", message_text.split("\n")[0])

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:

        driver.quit()


if __name__ == "__main__":
    login_and_get_message()
