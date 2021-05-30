from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('input Table in search field')
def search_amazon(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order', Keys.ENTER)


@when('Click on Amazon search icon')
def click_search(context):
    context.driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-search']").click()


@then('Verify search worked')
def verify_search(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
    print(f'Actual result: {actual_result}')
    expected_result = "Cancel Items or Orders"
    # verify
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    print("Test Passed")
