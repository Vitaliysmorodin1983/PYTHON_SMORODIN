from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru/")
driver.get("https://vk.com/")
driver.set_window_size(640, 460)

sleep(10)

driver.save_screenshot("./ya.png")

sleep(50) #установили «засыпание» браузера на 50 секунд