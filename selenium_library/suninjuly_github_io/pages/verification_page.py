import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.suninjuly_github_io.pages.base_page import BasePage


class VerificationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.url = 'https://suninjuly.github.io/wait2.html'
        self.verify_button_locator = ('css selector', '#verify')
        self.message_locator = ('css selector', '#verify_message')

    @property
    @allure.step('Verify button')
    def verify_button(self):
        return WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(self.verify_button_locator)
        )

    @property
    @allure.step('Message')
    def message(self):
        return self.find(self.message_locator)

    @allure.step('Assert success message')
    def should_be_success_message(self):
        assert 'success' in self.message.text.lower()
