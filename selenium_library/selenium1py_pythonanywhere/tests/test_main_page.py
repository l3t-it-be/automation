import pytest
from selenium_library.selenium1py_pythonanywhere.pages.basket_page import (
    BasketPage,
)
from selenium_library.selenium1py_pythonanywhere.pages.login_page import (
    LoginPage,
)
from selenium_library.selenium1py_pythonanywhere.pages.main_page import (
    MainPage,
)
from selenium_library.selenium1py_pythonanywhere.test_data.languages import (
    choices,
)


@pytest.mark.main_page
@pytest.mark.guest
@pytest.mark.regression
@pytest.mark.parametrize('language', choices.keys())
class TestMainPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser, language):
        choice = choices[language]['url']

        self.main_page = MainPage(browser)
        self.login_page = LoginPage(browser)
        self.basket_page = BasketPage(browser)

        self.main_page.open_page(self.main_page.url + choice)

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self):
        self.main_page.login_link_is_visible_and_clickable()

    @pytest.mark.smoke
    def test_guest_should_see_search_button(self):
        self.main_page.search_button_is_visible_and_clickable()

    @pytest.mark.smoke
    def test_guest_can_go_to_login_page(self):
        self.main_page.login_link.click()
        self.login_page.should_be_on_login_page()

    def test_guest_should_see_basket_link(self):
        self.main_page.basket_link_is_visible_and_clickable()

    @pytest.mark.basket
    def test_guest_cant_see_products_in_basket_opened_from_main_page(self):
        self.main_page.basket_link.click()
        self.basket_page.basket_should_be_empty()
        self.basket_page.empty_basket_should_have_message_about_it()
