from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@when('input Table in search field')
def search_amazon(context):
    table = context.driver.find_element(By.CSS_SELECTOR, 'span.a-color-state').send_keys('Table', Keys.ENTER)

@then('Verify search worked')
def verify_search(context):
    actual_result = table
    print(f'Actual result: {actual_result}')
    expected_result = '"table"'
    # verify
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    print("Test Passed")

