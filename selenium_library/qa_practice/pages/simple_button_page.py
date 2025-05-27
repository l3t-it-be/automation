from selenium.webdriver.common.by import By

from selenium_library.qa_practice.pages.base_page import BasePage


class SimpleButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.url = 'https://www.qa-practice.com/elements/button/simple'
        self.simple_button_locator = (By.CSS_SELECTOR, '#submit-id-submit')

    @property
    def simple_button(self):
        return self.find(self.simple_button_locator)
