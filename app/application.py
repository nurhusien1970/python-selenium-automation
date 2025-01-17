from pages.amazon_homepage import AmazonHomepage
from pages.header_order_department import Order
from pages.verify_order_sigin import VerifyOrderSignIn
from pages.cart_icon_page import Cart
from pages.verify_cart_icon import CartIcon
from pages.department_page import AllDept


class Applications:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = AmazonHomepage(self.driver)
        self.order_page = Order(self.driver)
        self.sign_in_page = VerifyOrderSignIn(self.driver)
        self.cart_click_page = Cart(self.driver)
        self.cart_click_result_page = CartIcon(self.driver)
        self.all_department_page = AllDept(self.driver)
