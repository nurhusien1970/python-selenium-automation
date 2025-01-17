from selenium.webdriver.common.by import By
from behave import given, when, then


@given('best Amazon sellers page')
def best_seller_tab(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@when('Find Best sellers tabs')
def best_sellers_nav_box(context):

    context.window = context.driver.find_elements(By.CSS_SELECTOR, 'div#zg_tabs ul a')


@then('Verify {nav_link} boxes are present')
def verify_count_box(context, nav_link):
    count_tabs = len(context.driver.find_elements(By.CSS_SELECTOR, 'div#zg_tabs ul a'))
    nav_link = int(nav_link)
    assert nav_link == count_tabs, f'expected {nav_link}, but got {count_tabs}'


@then('loop 5 links and verify they match the side menu text')
def loop_five_links(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    count = context.driver.find_elements(By.CSS_SELECTOR, 'div#zg_tabs ul a')

    for i in count:
        i.click()
        assert i.text in count[i]

