import allure

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

    @allure.step('Assert Login page contains its url and browser title')
    def should_be_login_page(self):
        self.url_should_contain_text(self.text_in_url)
        self.browser_title_should_contain_text(self.text_in_browser_title)

    @property
    @allure.step('Email input on Login page')
    def login_email_input(self):
        return self.find(self.login_email_input_locator)

    @property
    @allure.step('Password input on Login page')
    def login_password_input(self):
        return self.find(self.login_password_input_locator)

    @property
    @allure.step('Checkbox "Stay Logged In" on Login page')
    def stay_logged_in_checkbox(self):
        return self.find(self.stay_logged_in_checkbox_locator)

    @property
    @allure.step('Submit button on Login page')
    def submit_button(self):
        return self.find(self.submit_button_locator)

    @allure.step('Assert email input on Login page is visible and active')
    def assert_login_email_input_is_active(self):
        self.element_is_visible_and_enabled(
            self.login_email_input, 'Email input on Login page'
        )

    @allure.step('Assert password input on Login page is visible and active')
    def assert_login_password_input_is_active(self):
        self.element_is_visible_and_enabled(
            self.login_password_input, 'Password input on Login page'
        )

    @allure.step(
        'Assert checkbox "Stay Logged In" on Login page is visible and active'
    )
    def assert_stay_logged_in_checkbox_is_active(self):
        self.element_is_visible_and_enabled(
            self.stay_logged_in_checkbox,
            '"Stay Logged In" checkbox on Login page',
        )

    @allure.step('Assert Submit button on Login page is visible and clickable')
    def assert_submit_button_is_active(self):
        self.element_is_visible_and_enabled(
            self.submit_button,
            '"Submit" button on Login page',
        )

    @property
    @allure.step(
        'Actual max length of text in email input field on Login page'
    )
    def login_email_input_max_length_actual(self):
        return self.element_max_length(self.login_email_input)

    @property
    @allure.step(
        'Actual max length of text in password input field on Login page'
    )
    def login_password_input_max_length_actual(self):
        return self.element_max_length(self.login_password_input)

    @allure.step(
        'Assert max length of text in email input field on Login page equals the expected one'
    )
    def assert_login_email_input_max_length(self):
        assert (
            int(self.login_email_input_max_length_actual)
            == self.login_email_input_max_length_expected
        ), f'Email input field should have max length of {self.login_email_input_max_length_expected}'

    @allure.step(
        'Assert max length of text in password input field on Login page equals the expected one'
    )
    def assert_login_password_input_max_length(self):
        assert (
            int(self.login_password_input_max_length_actual)
            == self.login_password_input_max_length_expected
        ), f'Password input field should have max length of {self.login_password_input_max_length_expected}'

    @allure.step(
        'Assert text in email input field on Login page matches the one typed'
    )
    def assert_login_email_input_value(self):
        assert (
            self.element_value(self.login_email_input)
            == self.login_email_input_value
        ), f'Email input value should have {self.login_email_input_value}'

    @allure.step(
        'Assert text in password input field on Login page matches the one typed'
    )
    def assert_login_password_input_value(self):
        assert (
            self.element_value(self.login_password_input)
            == self.login_password_input_value
        ), f'Password input value should have {self.login_password_input_value}'

    @allure.step('Fill out email field on Login page')
    def fill_out_login_email_input(self):
        self.login_email_input.clear()
        self.login_email_input.send_keys(self.login_email_input_value)
        self.assert_login_email_input_value()

    @allure.step('Fill out password field on Login page')
    def fill_out_login_password_input(self):
        self.login_password_input.clear()
        self.login_password_input.send_keys(self.login_password_input_value)
        self.assert_login_password_input_value()
