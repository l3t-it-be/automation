from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.stepik.pages.base_page import BasePage
from selenium_library.stepik.test_data.credentials import (
    login_email,
    login_password,
)


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.url = 'https://stepik.org/catalog'
        self.log_in_button_locator = (
            By.CSS_SELECTOR,
            'a[href="/catalog?auth=login"]',
        )
        self.login_email_input_locator = (By.CSS_SELECTOR, '#id_login_email')
        self.login_password_input_locator = (
            By.CSS_SELECTOR,
            '#id_login_password',
        )
        self.submit_log_in_button_locator = (
            By.CSS_SELECTOR,
            'button[type="submit"]',
        )

    @property
    def log_in_button(self):
        return WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(self.log_in_button_locator)
        )

    def input_email(self):
        self.find(self.login_email_input_locator).send_keys(login_email)

    def input_password(self):
        self.find(self.login_password_input_locator).send_keys(login_password)

    def click_submit_log_in_button(self):
        self.find(self.submit_log_in_button_locator).click()

    def fill_out_login_form(self):
        self.input_email()
        self.input_password()
        self.click_submit_log_in_button()
