import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step('Open page')
    def open_page(self, url):
        return self.browser.get(url)

    @allure.step('Find element')
    def find(self, args):
        return self.browser.find_element(*args)

    @staticmethod
    @allure.step('Assert element actual text matches the one expected')
    def element_get_expected_text(element, expected_text, name):
        assert (
            element.text == expected_text
        ), f'{name} should have text "{expected_text}", but got "{element.text} instead"'
