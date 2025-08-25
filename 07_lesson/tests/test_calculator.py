from pages.calculator_page import CalculatorPage
import time


def test_calculator_with_delay(driver):
    calculator_page = CalculatorPage(driver)
    
    # Открываем калькулятор
    calculator_page.open()
    
    # Проверяем что страница загрузилась
    assert "calculator" in driver.current_url
    
    # Устанавливаем задержку 5 секунд вместо 45 для тестирования
    calculator_page.set_delay(5)
    
    # Даем время для применения задержки
    time.sleep(2)
    
    # Выполняем вычисления
    calculator_page.click_button('7')
    calculator_page.click_button('+')
    calculator_page.click_button('8')
    calculator_page.click_button('=')
    
    # Ждем результат
    timeout = 15
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        result = calculator_page.get_result()
        if result == '15':
            break
        time.sleep(1)
    else:
        result = calculator_page.get_result()
        assert False, f'Expected 15, got {result} after {timeout}s'
    
    assert result == '15'