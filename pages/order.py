from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from time import sleep


class Order(Page):
    ORDER_LINK = (By.CSS_SELECTOR, "a[href ='/gp/css/order-history?ref_=nav_orders_first'] span.nav-line-1")

# ORDER_LINK= (By.CSS_SELECTOR, "a.nav-a.nav-a-2.nav-progressive-attribute[
    # href='/gp/css/order-history?ref_=nav_orders_first")

    def wait(self):
        self.wait_for_element_click(self, *self.ORDER_LINK)

    def click_order_link(self):
        self.click(*self.ORDER_LINK)
        sleep(10)



