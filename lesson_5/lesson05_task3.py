from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def input_operations():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    try:

        driver.get("http://the-internet.herokuapp.com/inputs")

        input_field = driver.find_element(By.TAG_NAME, "input")

        input_field.send_keys("Sky")

        input_field.clear()

        input_field.send_keys("Pro")

        import time
        time.sleep(4)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:

        driver.quit()


if __name__ == "__main__":
    input_operations()
