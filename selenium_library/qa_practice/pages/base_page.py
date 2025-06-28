import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.result_locator = ('css selector', '#result-text')

    @allure.step('Open page')
    def open_page(self, url):
        self.browser.set_window_size(1920, 1080)
        self.browser.get(url)
        return self.browser.get(url)

    @allure.step('Find element')
    def find(self, args):
        return self.browser.find_element(*args)

    @property
    @allure.step('Result')
    def result(self):
        return self.find(self.result_locator)

    @allure.step('Assert expected text is visible')
    def text_should_appear(self, expected_text):
        assert (
            self.result.text == expected_text
        ), f'If button was clicked, there should be {expected_text}"'
