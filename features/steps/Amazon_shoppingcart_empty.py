from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('Amazon Open Page logo')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/ref=nav_logo')


@when('Click Amazon logo')
def click_amazon_logo(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div#nav-cart-count-container span.nav-cart-icon.nav-sprite').click()


@when('User clicks Shopping Cart Icon')
def search_amazon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a#nav-logo-sprites').click()
