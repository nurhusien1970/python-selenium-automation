from selenium.webdriver.common.by import By
from behave import given, then


# from selenium.webdriver.common.keys import Keys


@given("Wholefoods Page")
def wholefoods_open(context):
    context.driver.get('https://www.amazon.com/fmc/storedeals/?_encoding=UTF8&almBrandId=VUZHIFdob2xlIEZvb2Rz')


@then('If locator list is {length:d} for any bottom item')
def verify_length(context, length):
    context.driver.implicitly_wait(6)
    product_list = context.driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium.a-padding-none.a'
                                                                 '-text-left '
                                                                 'span.a-size-extra-large.wfm-sales-item-card__prime'
                                                                 '-price.a-text-bold')
    print(product_list)
    print(len(product_list))
    assert len(product_list) == int(length), f'error, expected {length}, actual is {product_list}'
