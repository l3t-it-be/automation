import pytest

from selenium_library.selenium1py_pythonanywhere.pages.base_page import (
    BasePage,
)
from selenium_library.selenium1py_pythonanywhere.pages.basket_page import (
    BasketPage,
)
from selenium_library.selenium1py_pythonanywhere.pages.login_page import (
    LoginPage,
)
from selenium_library.selenium1py_pythonanywhere.pages.product_page import (
    ProductPage,
)
from selenium_library.selenium1py_pythonanywhere.test_data.languages import (
    choices,
)


@pytest.mark.product_page
@pytest.mark.guest
@pytest.mark.regression
@pytest.mark.parametrize('language', choices.keys())
class TestProductPageAsGuest:
    @pytest.fixture(autouse=True)
    def setup(self, browser, language):
        choice = choices[language]['url']
        self.base_url = (
            f'https://selenium1py.pythonanywhere.com/{choice}/catalogue/'
        )
        self.product_page = ProductPage(browser)
        self.login_page = LoginPage(browser)
        self.basket_page = BasketPage(browser)

    def _get_product_url(self, product_path):
        return f'{self.base_url}{product_path}'

    @pytest.mark.smoke
    def test_add_to_cart_button_is_displayed(self, browser, language):
        url = self._get_product_url('the-art-of-the-start_169/')
        self.product_page.open_page(url)
        self.product_page.add_to_basket_button_is_visible_and_clickable()
        self.product_page.add_to_basket_button_should_have_text(
            choices[language]['button_text']
        )

    @pytest.mark.smoke
    @pytest.mark.promo
    def test_guest_can_add_new_year_promo_product_to_basket(self, browser):
        url = self._get_product_url(
            'the-shellcoders-handbook_209/?promo=newYear'
        )
        self.product_page.open_page(url)
        self.product_page.should_be_promo_new_year_product_page()
        self.product_page.add_product_to_basket()

    @pytest.mark.smoke
    def test_guest_should_see_login_link_on_product_page(self, browser):
        url = self._get_product_url(
            'the-girl-who-kicked-the-hornets-nest_199/'
        )
        self.product_page.open_page(url)
        self.product_page.login_link_is_visible_and_clickable()

    @pytest.mark.smoke
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        url = self._get_product_url('learning-python_121/')
        self.product_page.open_page(url)
        self.product_page.login_link.click()
        self.login_page.should_be_on_login_page()

    @pytest.mark.promo
    @pytest.mark.parametrize(
        'offer_number',
        # fmt: off
    ['0', '1', '2', '3', '4', '5','6',
        pytest.param('7', marks=pytest.mark.xfail),
        '8', '9']
        # fmt: on
    )
    def test_guest_can_add_promo_offer_product_to_basket(
        self, browser, offer_number
    ):
        url = self._get_product_url(
            f'coders-at-work_207/?promo=offer{offer_number}'
        )
        self.product_page.open_page(url)
        self.product_page.should_be_promo_offer_product_page(offer_number)
        self.product_page.add_product_to_basket()

    @pytest.mark.basket
    def test_guest_cant_see_product_in_basket_opened_from_product_page(
        self, browser
    ):
        url = self._get_product_url('the-girl-with-the-dragon-tattoo_194/')
        self.product_page.open_page(url)
        self.product_page.basket_link.click()
        self.basket_page.basket_should_be_empty()
        self.basket_page.empty_basket_should_have_message_about_it()

    def test_guest_cant_see_success_message(self, browser):
        url = self._get_product_url('the-girl-who-played-with-non-fire_203/')
        self.product_page.open_page(url)
        self.product_page.should_not_have_success_message()


@pytest.mark.product_page
@pytest.mark.user
@pytest.mark.regression
@pytest.mark.parametrize('language', choices.keys())
class TestProductPageAsAuthenticatedUser:
    @pytest.fixture(autouse=True)
    def setup(self, browser, language, random_generator):
        self.base_page = BasePage(browser)
        self.login_page = LoginPage(browser)
        self.product_page = ProductPage(browser)

        choice = choices[language]['url']
        base_url = f'{self.base_page.url}{choice}/accounts/login/'
        self.login_page.open_page(base_url)

        email, password = random_generator.email(), random_generator.password()
        self.login_page.register_new_user(email, password)
        self.base_page.should_be_authorized_user(email)

        self.product_base_url = f'{self.base_page.url}{choice}/catalogue/'

    def _get_product_url(self, product_path):
        return f'{self.product_base_url}{product_path}'

    @pytest.mark.smoke
    @pytest.mark.promo
    def test_user_can_add_product_to_basket(self, browser):
        url = self._get_product_url(
            'the-shellcoders-handbook_209/?promo=newYear'
        )
        self.product_page.open_page(url)
        self.product_page.add_product_to_basket()

    def test_user_cant_see_success_message(self, browser):
        url = self._get_product_url('the-clean-coder_150/')
        self.product_page.open_page(url)
        self.product_page.should_not_have_success_message()
