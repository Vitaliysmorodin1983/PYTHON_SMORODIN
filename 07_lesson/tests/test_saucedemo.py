from pages.login_page import LoginPage
from pages.cart_page import CartPage
#import time


def test_saucedemo_checkout(driver):
    login_page = LoginPage(driver)
    
    products_page = login_page.open().login('standard_user', 'secret_sauce')

    #time.sleep(4)
    cart_page = products_page.add_products_to_cart().go_to_cart()
    #time.sleep(4)
    checkout_page = cart_page.checkout()
    #time.sleep(4)
    checkout_page.fill_checkout_info('John', 'Doe', '12345')
    #time.sleep(4)
    total_amount = checkout_page.get_total_amount()
    assert total_amount == '58.29'