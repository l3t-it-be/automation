import pytest

from selenium_library.qa_practice.pages.like_a_button_page import (
    LikeAButtonPage,
)


@pytest.mark.regression
class TestLikeButtonPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.like_a_button_page = LikeAButtonPage(browser)
        self.like_a_button_page.open_page(self.like_a_button_page.url)

    @pytest.mark.smoke
    def test_like_a_button_is_displayed(self, browser):
        assert self.like_a_button_page.like_a_button.is_displayed()

    @pytest.mark.smoke
    def test_like_a_button_is_clickable(self, browser):
        self.like_a_button_page.like_a_button.click()
        self.like_a_button_page.text_should_appear('Submitted')
