from pages.calculator_page import CalculatorPage


def test_calculator_with_delay(driver):
    calculator_page = CalculatorPage(driver)
    
    calculator_page.open().set_delay(45)
    calculator_page.perform_calculation()
    result = calculator_page.wait_for_result('15')
    
    assert result == '15'