import pytest

from selenium_library.qa_practice.pages.simple_button_page import (
    SimpleButtonPage,
)


@pytest.mark.regression
class TestSimpleButtonPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.simple_button_page = SimpleButtonPage(browser)
        self.simple_button_page.open_page(self.simple_button_page.url)

    @pytest.mark.smoke
    def test_simple_button_is_displayed(self, browser):
        assert self.simple_button_page.simple_button.is_displayed()

    @pytest.mark.smoke
    def test_simple_button_is_clickable(self, browser):
        self.simple_button_page.simple_button.click()
        self.simple_button_page.text_should_appear('Submitted')
