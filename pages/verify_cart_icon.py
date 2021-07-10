from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from time import sleep


class CartIcon(Page):
    # "//h1.a-spacing-mini.a-spacing-top-base")
    #ICON = (By.XPATH, "//h1[@class='a-spacing-mini a-spacing-top-base']")
   # expected_text = "Your Amazon Cart is empty."
    #expected_url = "https://www.amazon.com/gp/cart/view.html?ref_=nav_cart"

    # def wait(self):
    # self.wait = WebDriverWait(self.driver, 10)
    #    self.wait_for_element_appear(self, *self.ICON)

    #sleep(3)

   # def cart_icon_text(self):
   #     sleep(10)
    #    self.verify_text(self.expected_text, *self.ICON)
    #    sleep(6)

    def current_empty_cart_url(self, expected_url):
        self.current_url(expected_url)


