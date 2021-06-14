@given('Amazon Open Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Search {search_word}')
def search_product_cart(context, search_word):
    cart_search = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    cart_search.clear()
    cart_search.send_keys(search_word, Keys.ENTER)
    sleep(100)


@when('Click first product')
def click_any_product(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.a-size-base-plus.a-color-base.a-text-normal').click()


@when('Click add to cart')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input#add-to-cart-button').click()

@when('Click add next')
def click_add_to_cart_next(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span#attachSiAddCoverage').click()


@then('Verify item is in cart')
def item_added(context):
    cart_added = context.driver.find_element(By.CSS_SELECTOR, 'div#nav-cart-count-container').text
    print(cart_added)
    sleep(5)
    assert cart_added == '0'
    cart_added = context.driver.find_element(By.CSS_SELECTOR, 'div#nav-cart-count-container').text
    print(cart_added)
    assert cart_added != '0'
    print("Omar is Awesome!")
