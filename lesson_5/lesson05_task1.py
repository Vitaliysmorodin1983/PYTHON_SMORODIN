from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def click_blue_button():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:

        driver.get("http://uitestingplayground.com/classattr")

        blue_button = driver.find_element(
            By.XPATH, "//button[contains(concat(' ', @class, ' '), ' btn-primary ')]")
        blue_button.click()

        driver.implicitly_wait(2)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:

        driver.quit()


if __name__ == "__main__":
    click_blue_button()
