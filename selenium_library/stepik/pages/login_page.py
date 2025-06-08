import os

from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.stepik.pages.base_page import BasePage

load_dotenv()


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.url = 'https://stepik.org/catalog'
        self.log_in_button_locator = (
            'css selector',
            'a[href="/catalog?auth=login"]',
        )
        self.login_email_input_locator = ('css selector', '#id_login_email')
        self.login_password_input_locator = (
            'css selector',
            '#id_login_password',
        )
        self.submit_log_in_button_locator = (
            'css selector',
            'button[type="submit"]',
        )

    @property
    def log_in_button(self):
        return WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(self.log_in_button_locator)
        )

    def input_email(self):
        self.find(self.login_email_input_locator).send_keys(
            os.environ['LOGIN_EMAIL']
        )

    def input_password(self):
        self.find(self.login_password_input_locator).send_keys(
            os.environ['LOGIN_PASSWORD']
        )

    def click_submit_log_in_button(self):
        self.find(self.submit_log_in_button_locator).click()

    def fill_out_login_form(self):
        self.input_email()
        self.input_password()
        self.click_submit_log_in_button()
