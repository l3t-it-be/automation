from selenium_library.browser_setup import random_generator
from selenium_library.freeconferencecall.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.text_in_url = 'login'
        self.text_in_browser_title = 'Log in page'

        self.login_email_input_locator = (
            'css selector',
            'input[type="email"]',
        )
        self.login_email_input_max_length_expected = 64
        self.login_email_input_value = random_generator.email()

        self.login_password_input_locator = (
            'css selector',
            'input[type="password"]',
        )
        self.login_password_input_max_length_expected = 32
        self.login_password_input_value = random_generator.password()

        self.stay_logged_in_checkbox_locator = (
            'css selector',
            'input[name="rememberme"]',
        )

        self.submit_button_locator = ('css selector', 'button#loginformsubmit')

    def should_be_login_page(self):
        self.url_should_contain_text(self.text_in_url)
        self.browser_title_should_contain_text(self.text_in_browser_title)

    @property
    def login_email_input(self):
        return self.find(self.login_email_input_locator)

    @property
    def login_password_input(self):
        return self.find(self.login_password_input_locator)

    @property
    def stay_logged_in_checkbox(self):
        return self.find(self.stay_logged_in_checkbox_locator)

    @property
    def submit_button(self):
        return self.find(self.submit_button_locator)

    def assert_login_email_input_is_active(self):
        self.element_is_visible_and_enabled(
            self.login_email_input, 'Email input on Login page'
        )

    def assert_login_password_input_is_active(self):
        self.element_is_visible_and_enabled(
            self.login_password_input, 'Password input on Login page'
        )

    def assert_stay_logged_in_checkbox_is_active(self):
        self.element_is_visible_and_enabled(
            self.stay_logged_in_checkbox,
            '"Stay Logged In" checkbox on Login page',
        )

    def assert_submit_button_is_active(self):
        self.element_is_visible_and_enabled(
            self.submit_button,
            '"Submit" button on Login page',
        )

    @property
    def login_email_input_max_length_actual(self):
        return self.element_max_length(self.login_email_input)

    @property
    def login_password_input_max_length_actual(self):
        return self.element_max_length(self.login_password_input)

    def assert_login_email_input_max_length(self):
        assert (
            int(self.login_email_input_max_length_actual)
            == self.login_email_input_max_length_expected
        ), f'Email input field should have max length of {self.login_email_input_max_length_expected}'

    def assert_login_password_input_max_length(self):
        assert (
            int(self.login_password_input_max_length_actual)
            == self.login_password_input_max_length_expected
        ), f'Password input field should have max length of {self.login_password_input_max_length_expected}'

    def assert_login_email_input_value(self):
        assert (
            self.element_value(self.login_email_input)
            == self.login_email_input_value
        ), f'Email input value should have {self.login_email_input_value}'

    def assert_login_password_input_value(self):
        assert (
            self.element_value(self.login_password_input)
            == self.login_password_input_value
        ), f'Password input value should have {self.login_password_input_value}'

    def fill_out_login_email_input(self):
        self.login_email_input.clear()
        self.login_email_input.send_keys(self.login_email_input_value)
        self.assert_login_email_input_value()

    def fill_out_login_password_input(self):
        self.login_password_input.clear()
        self.login_password_input.send_keys(self.login_password_input_value)
        self.assert_login_password_input_value()
