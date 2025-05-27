import pytest

from selenium_library.suninjuly_github_io.pages.verification_page import (
    VerificationPage,
)


@pytest.mark.regression
class TestVerification:
    @pytest.mark.smoke
    def test_successful_verification(self, browser):
        verification_page = VerificationPage(browser)
        verification_page.open_page(verification_page.url)

        verification_page.verify_button.click()
        verification_page.should_be_success_message()
