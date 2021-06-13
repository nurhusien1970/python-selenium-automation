from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep


@given('Open Amazon help Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@given('open help page')
def open_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('help search icon')
def search_amazon(context):
    help_search = context.driver.find_element(By.CSS_SELECTOR, 'div input#helpsearch').send_keys('Cancel Order', Keys.ENTER)
    print(help_search)
    sleep(10)

    sleep(10)

@then('cancel item worked')
def search(context):
        cancel_result = context.driver.find_element(By.CSS_SELECTOR, 'div.help-content h1').text
        # print(f'Actual result: {actual_result}')
        cancel_expected_result = "Cancel Items or Orders"
        # verify
        assert cancel_expected_result == cancel_result, f'Expected {cancel_expected_result}, but got {cancel_result}'
        print("Test Passed")

