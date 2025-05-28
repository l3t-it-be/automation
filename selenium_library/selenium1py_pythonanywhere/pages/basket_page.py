from selenium_library.selenium1py_pythonanywhere.pages.base_page import (
    BasePage,
)


class BasketPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.basket_items_locator = ('css selector', '.basket-items')
        self.empty_basket_message_locator = (
            'css selector',
            '#content_inner p',
        )

    def basket_should_be_empty(self):
        assert self.element_is_not_present(self.basket_items_locator)

    def empty_basket_should_have_message_about_it(self):
        assert self.find(
            self.empty_basket_message_locator
        ).is_displayed(), (
            'Empty basket should have message that it is empty, but it has not'
        )
