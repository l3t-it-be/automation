import pytest
from selenium.common import NoSuchElementException

from selenium_library.suninjuly_github_io.pages.registration_page import (
    RegistrationPage,
)
from selenium_library.suninjuly_github_io.test_data.registration import (
    right_url,
    wrong_url,
)


@pytest.mark.regression
class TestRegistrationPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.registration_page = RegistrationPage(browser)

    @pytest.mark.smoke
    def test_successful_registration(self, browser, random_generator):
        self.registration_page.open_page(right_url)
        self.registration_page.fill_out_the_form(random_generator)
        self.registration_page.should_have_welcome_text()

    @pytest.mark.xfail(reason='wrong url')
    def test_failed_registration(self, browser, random_generator):
        self.registration_page.open_page(wrong_url)
        try:
            self.registration_page.fill_out_the_form(random_generator)
        except NoSuchElementException:
            print('Element not found on the page')
        self.registration_page.should_have_welcome_text()
