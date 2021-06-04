from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep


@then('Click add to cart')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "img.s-image").click()
    context.driver.find_element(By.ID, 'a-button-input').click()
    sleep(100)


@then('Verify item is added')
def item_not_empty(context):
    pass