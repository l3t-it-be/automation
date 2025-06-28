import allure

from selenium_library.qa_practice.pages.base_page import BasePage


class SimpleButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.url = 'https://www.qa-practice.com/elements/button/simple'
        self.simple_button_locator = ('css selector', '#submit-id-submit')

    @property
    @allure.step('Simple button')
    def simple_button(self):
        return self.find(self.simple_button_locator)
