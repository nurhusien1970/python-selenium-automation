from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@then('Shopping Cart is Empty')
def verify_search(context):
    actual_result = context.driver.current_url
    print(f'Actual result: {actual_result}')
    expected_result = 'https://www.amazon.com/gp/cart/view.html?ref_=nav_cart'
    # verify
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    print("Test Passed")