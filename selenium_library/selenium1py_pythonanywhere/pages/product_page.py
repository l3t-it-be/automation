import allure

from selenium_library.selenium1py_pythonanywhere.pages.base_page import (
    BasePage,
)


class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.add_to_basket_button_locator = (
            'css selector',
            'button.btn-add-to-basket',
        )
        self.new_year_text_in_url = '?promo=newYear'
        self.success_message_locator = ('css selector', '.alertinner')
        self.product_name_locator = ('css selector', '.product_main h1')
        self.product_name_in_message_locator = (
            'css selector',
            '.alertinner strong',
        )
        self.product_price_locator = ('css selector', 'p.price_color')
        self.product_price_in_message_locator = (
            'css selector',
            '.alertinner p strong',
        )

    @allure.step('Assert product Promo New Year page contains its text in URL')
    def should_be_promo_new_year_product_page(self):
        self.url_should_contain_text(self.new_year_text_in_url)

    @allure.step('Assert product Promo Offer page contains its text in URL')
    def should_be_promo_offer_product_page(self, promo_offer):
        self.url_should_contain_text(promo_offer)

    @property
    @allure.step('Add to basket button')
    def add_to_basket_button(self):
        return self.find(self.add_to_basket_button_locator)

    @allure.step(
        'Assert Add to basket button on product page is visible and clickable'
    )
    def add_to_basket_button_is_visible_and_clickable(self):
        self.element_is_visible_and_enabled(
            self.add_to_basket_button, 'Add to basket button'
        )

    @allure.step('Assert Add to basket button has its text')
    def add_to_basket_button_should_have_text(self, expected_text):
        self.element_get_expected_text(
            self.add_to_basket_button, expected_text, 'Add to basket button'
        )

    @allure.step('Assert success message is displayed')
    def should_have_success_message(self):
        assert self.find(
            self.success_message_locator
        ).is_displayed(), 'Success message is not presented, but should be'

    @allure.step('Assert success message is not displayed')
    def should_not_have_success_message(self):
        assert self.element_is_not_present(
            self.success_message_locator
        ), 'Success message is presented, but should not be'

    @allure.step('Assert product name matches the one added to basket')
    def product_name_should_match_the_one_added(self):
        product_name = self.find(self.product_name_locator).text
        product_name_in_message = self.find(
            self.product_name_in_message_locator
        ).text
        assert (
            product_name == product_name_in_message
        ), 'Product name does not match the one added to basket'

    @allure.step('Assert product price matches original product price')
    def product_price_should_match_original_product_price(self):
        product_price = self.find(self.product_price_locator).text
        product_price_in_message = self.find(
            self.product_price_in_message_locator
        ).text
        assert (
            product_price == product_price_in_message
        ), 'Product price does not match original product price'

    def add_product_to_basket(self):
        self.add_to_basket_button.click()
        self.solve_quiz_and_get_code()
        self.should_have_success_message()
        self.product_name_should_match_the_one_added()
        self.product_price_should_match_original_product_price()
