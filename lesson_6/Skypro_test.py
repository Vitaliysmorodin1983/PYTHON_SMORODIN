from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService


service = EdgeService(r"C:\Users\smoro\Downloads\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)

try:

    driver.get("http://uitestingplayground.com/textinput")

    text_input = driver.find_element(By.ID, "newButtonName")
    text_input.clear()
    text_input.send_keys("SkyPro")

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

    button_text = driver.find_element(By.ID, "updatingButton").text
    print(button_text)

finally:

    driver.quit()
