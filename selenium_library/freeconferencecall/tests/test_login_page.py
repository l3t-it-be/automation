import pytest

from selenium_library.freeconferencecall.pages.base_page import BasePage
from selenium_library.freeconferencecall.pages.login_page import LoginPage


@pytest.mark.login_page
@pytest.mark.regression
class TestLoginPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.base_page = BasePage(browser)
        self.base_page.open_main_page()
        self.base_page.open_login_page()
        self.login_page = LoginPage(browser)

    @pytest.mark.smoke
    def test_login_form(self, browser):
        self.login_page.should_be_login_page()

        self.login_page.assert_login_email_input_is_active()
        self.login_page.assert_login_email_input_max_length()
        self.login_page.fill_out_login_email_input()

        self.login_page.assert_login_password_input_is_active()
        self.login_page.assert_login_password_input_max_length()
        self.login_page.fill_out_login_password_input()

        self.login_page.assert_gdpr_checkbox_is_active()
        self.login_page.assert_stay_logged_in_checkbox_is_active()
        self.login_page.assert_submit_button_is_active()
