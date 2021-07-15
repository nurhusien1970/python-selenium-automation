from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def hover_cursor(self, *locator):
        new_arrivals = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()
        sleep(10)

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element_click(self, *locator):
        e = self.wait.until(ec.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(ec.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def verify_text(self, expected_text, *locator):
        sleep(10)
        actual_text = self.driver.find_element(*locator).text
        sleep(10)
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_text_in(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} in {actual_text}, but got {actual_text}'

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'{query} not in {self.driver.current_url}'

    def current_url(self, expected_url):
        # assert self.driver.current_url == expected_url, f'{expected_url} not equal {self.driver.current_url}'

        if self.driver.current_url == expected_url:
            print("pass")

        else:
            print("failed")
