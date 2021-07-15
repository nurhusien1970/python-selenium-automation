from behave import given, when, then


@given('Amazon Open Product Page')
def product_page(context):
    context.app.all_department_page.open_products_page()


@when('from the department dropdown select computers')
def department_select(context):
    context.app.all_department_page.dropdown_select()


@when('hover over the New Arrivals')
def move_cursor(context):
    context.app.all_department_page.move_cursor()


@when('click the department dropdown')
def department_all_click(context):
    context.app.all_department_page.click_all()


@then('Select store for computers')
def department_computer_click(context):
    context.app.all_department_page.click_all()


@then('verify you selected store for computers')
def verify_department(context):
    context.app.all_department_page.verify_department()


@then('Verify for New Arrivals')
def verify_new_arrivals(context):
    context.app.all_department_page.verify_new_arrivals()
