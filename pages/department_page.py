from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AllDept(Page):
    ALL_DEPT = (By.CSS_SELECTOR, "select#searchDropdownBox")
    COMP_LOCATION = (By.CSS_SELECTOR, ".nav-search-scope.nav-sprite")
    DEPARTMENT_ALL = (By.ID, "searchDropdownBox")
    COMP = (By.CSS_SELECTOR, "span.a-color-state.a-text-bold")
    TEXT = 'HP'
    PRODUCTS_OPEN_PAGE = 'https://www.amazon.com/gp/product/B074TBCSC8'
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[href ='/s/ref=sr_hi_2/?_encoding=UTF8&bbn=17020138011&ie=UTF8&qid=1498592471"
                                     "&rh=n%3A7141123011%2Cn%3A17020138011&ref_=sv_sl_6']")
    img = (By.CSS_SELECTOR, "img[src = 'https://m.media-amazon.com/images/G/01//AMAZON_FASHION/2021/SITE_FLIPS/SUM_1/SubNav/Summer_subnavBoys.jpg']")

    def click_all(self):
        self.click(*self.ALL_DEPT)
        self.click(*self.COMP_LOCATION)

    def dropdown_select(self):
        select = Select(self.find_element(*self.DEPARTMENT_ALL))
        select.select_by_value('search-alias=computers')

    def verify_department(self):
        self.verify_text_in(self.TEXT, *self.COMP)

    def open_products_page(self):
        self.open_url(self.PRODUCTS_OPEN_PAGE)

    def move_cursor(self):
        self.hover_cursor(*self.NEW_ARRIVALS)

    def verify_new_arrivals(self):
        self.wait_for_element_appear(*self.img)
