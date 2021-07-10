from pages.base_page import Page
from selenium.webdriver.common.by import By


class Cart(Page):
    CART_ICON = (By.CSS_SELECTOR, "span.nav-cart-icon.nav-sprite")

    def click_cart_icon(self):
        self.click(*self.CART_ICON)
