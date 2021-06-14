from selenium.webdriver.common.by import By
from behave import given, then


@given('Amazon {color_value} page')
def color_prod_page(context, color_value):
    context.driver.get(f'https://www.amazon.com/dp/{color_value}/')


@then('color product is looped over')
def color_prod_loop(context):
    expected_list = ['Black', 'Blue', 'Burgundy', 'Caramel', 'Gray', 'Green', 'Pink', 'White', 'Yellow']
# select the color list
    e_list = context.driver.find_elements(By.CSS_SELECTOR, "div.a-section #variation_color_name ul li")
    print(len(e_list))
    print(e_list)
    for i in range(len(e_list)):
        e_list[i].click()

        color_text = context.driver.find_element(By.CSS_SELECTOR, "div.a-section #variation_color_name span.selection").text
        print(color_text == expected_list[i])
        assert color_text == expected_list[i], f"error, expected {expected_list[i]} but got  {color_text}"

