from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def click_dynamic_button():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:

        driver.get("http://uitestingplayground.com/dynamicid")

        blue_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'btn-primary')]"))
        )
        blue_button.click()
        print("Успешно: кнопка нажата")

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:

        driver.quit()


if __name__ == "__main__":
    click_dynamic_button()
