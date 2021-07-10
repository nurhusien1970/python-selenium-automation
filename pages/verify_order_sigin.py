from pages.base_page import Page
from selenium.webdriver.common.by import By


class VerifyOrderSignIn(Page):
    SIGN_IN = (By.CSS_SELECTOR, "h1.a-spacing-small")
    EXPECTED_TEXT = "Sign-In"

    def verify_order(self):
        self.verify_text(self.EXPECTED_TEXT, *self.SIGN_IN)
