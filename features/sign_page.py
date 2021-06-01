from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@then('Verify Sign In page opens')
def sign_verify(context):
    var3 = context.driver.find_element(By.XPATH, '/div [.//text()[normalize-space()')
    assert 'Sign-In' == var3, f'result not in {var3}'
