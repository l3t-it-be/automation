from selenium.webdriver.common.by import By

from selenium_library.suninjuly_github_io.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class VerificationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.url = 'https://suninjuly.github.io/wait2.html'
        self.verify_button_locator = (By.CSS_SELECTOR, '#verify')
        self.message_locator = (By.CSS_SELECTOR, '#verify_message')

    @property
    def verify_button(self):
        return WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(self.verify_button_locator)
        )

    @property
    def message(self):
        return self.find(self.message_locator)

    def should_be_success_message(self):
        assert 'success' in self.message.text.lower()
