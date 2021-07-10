from pages.base_page import Page


class AmazonHomepage(Page):

    def homepage(self):
        self.open_url("https://www.amazon.com/")
