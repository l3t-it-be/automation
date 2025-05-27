from selenium.webdriver.common.by import By

from selenium_library.suninjuly_github_io.pages.base_page import BasePage
from selenium_library.suninjuly_github_io.test_data.registration import (
    welcome_text_expected,
)


class RegistrationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.first_name_input_locator = (
            By.CSS_SELECTOR,
            '.first_block input.first',
        )
        self.last_name_input_locator = (
            By.CSS_SELECTOR,
            '.first_block input.second',
        )
        self.email_input_locator = (
            By.CSS_SELECTOR,
            '.first_block input.third',
        )
        self.submit_button_locator = (By.CSS_SELECTOR, 'button')
        self.welcome_text_locator = (By.CSS_SELECTOR, 'h1')

    @property
    def first_name_input(self):
        return self.find(self.first_name_input_locator)

    @property
    def last_name_input(self):
        return self.find(self.last_name_input_locator)

    @property
    def email_input(self):
        return self.find(self.email_input_locator)

    @property
    def submit_button(self):
        return self.find(self.submit_button_locator)

    def fill_out_the_form(self, random_generator):
        self.first_name_input.send_keys(random_generator.first_name())
        self.last_name_input.send_keys(random_generator.last_name())
        self.email_input.send_keys(random_generator.email())
        self.submit_button.click()

    @property
    def welcome_text(self):
        return self.find(self.welcome_text_locator)

    def should_have_welcome_text(self):
        self.element_get_expected_text(
            self.welcome_text, welcome_text_expected, 'Welcome text'
        )
