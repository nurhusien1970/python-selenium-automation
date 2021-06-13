from behave import given, when, then
from selenium.webdriver.common.by import By


"""ui #1
#@given('Amazon page')
def amazon_page(context):
    context.driver('https://www.amazon.com/gp/help/customer/display.html')
"""

@when('hello on page')
def hello_can_i_help(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div.a-section h1')


@then('Verify if Hello. What ..help you with...')
def verify_hello(context):
    hello = context.driver.find_element(By.CSS_SELECTOR, 'div.a-span12.a-column.a-spacing-top-small')
    assert 'Hello. What can we help you with?' == hello

# scenario ui #2


@when("User sees 'Some things you can do here'")
def somethings(context):
    context.driver.find_elements(By.CSS_SELECTOR, 'div.a-column.a-span12')


@then('Verify number of tabs is {nine:d}')
def verify_amount(context, nine):
    somethings_count = len(context.driver.find_elements(By.CSS_SELECTOR, 'div.a-column.a-span12'))
    assert nine == somethings_count, f'wrong, expected {nine} but got {somethings_count}'


# scenario ui #3
@when("User checks the search box")
def help_library(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input#helpsearch')
    context.driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-search')


@then('Verify the search tab')
def help_search_tab(context):
    help_search = context.driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-search")
    print(help_search)
    assert "" == help_search
    help_search1 = context.driver.find_element(By.ID, 'i.a-icon.a-icon-search').text
    assert help_search1 == help_search


# scenario ui #4
@when('dropdown 12 elements')
def browse_help(context):
    context.driver.find_elements(By.CSS_SELECTOR, 'ul#category-section li')


@then('{twelve} elements are checked by loops')
def check_elements(context, twelve):
    twelve_counts1 = context.driver.find_elements(By.CSS_SELECTOR, 'div.csg-hover-box clearfix ul#category-section li')
    twelve_counts = context.driver.find_elements(By.XPATH, "//div[@class='csg-hover-box-categories']//ul["
                                                           "@id= 'category-section']//li")
    assert len(twelve_counts) == int(twelve)
    assert len(twelve_counts1) == int(twelve)
    html_list = context.driver.find_element_by_xpath("div[@class='csg-hover-box-categories']")
    items = html_list.find_elements_by_tag_name("li")
    for item in items:
        text = item.text
        print(text)

    print('twelve count is', twelve_counts, len(twelve_counts))
    assert len(twelve_counts) == int(twelve), f'wrong, expected {int(twelve)}, but got {len(twelve_counts)}'
    for _ in twelve_counts:
        assert twelve_counts[0].text == "Recommended Topics"
        assert twelve_counts[1].text == "Where's My Stuff?"
        assert twelve_counts[2].text == "Managing Your Orders"
        assert twelve_counts[3].text == "Managing Your Account"
        assert twelve_counts[4].text == "Returns & Refunds"
        assert twelve_counts[5].text == "Shipping Policies"
        assert twelve_counts[6].text == "Devices & Digital Services"
        assert twelve_counts[7].text == "Amazon Business Accounts"
        assert twelve_counts[8].text == "Large Items and Heavy-Bulky Services"
        assert twelve_counts[9].text == "Security & Privacy"
        assert twelve_counts[10].text == "Security & Privacy"
        assert twelve_counts[11].text == "Need More Help?"
    else:
        print('Lane is wrong')


# scenario ui #5
@then('Verify tools icon')
def check_recommended_topics(context):
    recommended = context.driver.find_elements(By.CSS_SELECTOR, 'li a.active').text
    assert recommended == "Recommended Topics ", f'wrong, expected {"Recommended Topics "}, but got {recommended}'


# scenario ui #6


@then('Check tools icon is present')
def check_tools_icon(context):
    icon = context.driver.find_elements(By.CSS_SELECTOR, 'img.csg-hb-promo')
    assert [] == icon, f'wrong, expected {[]} but got {icon}'
