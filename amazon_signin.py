from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@when('Click Sign In')
def Click_Sign_In(context):
    var1 = context.driver.find_element(By.CSS_SELECTOR, "a[href *= 'signin']").click()
    # $$("div#nav-tools a[href *= 'signin']") var2 = context.driver.find_element(By.XPATH, "//div[@class='a-box-inner
    # a-padding-extra-large']//h1[@class='a-spacing-small']").
    #print(var2)

@then('Verify Continue text as page opens')
def sign_verify(context):
    #context.driver.find_element(By.ID, 'continue').click()

    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url, f'wromg url{context.driver.current_url}'
    assert context.failed is False


