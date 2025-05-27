from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.result_locator = (By.CSS_SELECTOR, '#result-text')

    def open_page(self, url):
        return self.browser.get(url)

    def find(self, args):
        return self.browser.find_element(*args)

    @property
    def result(self):
        return self.find(self.result_locator)

    def text_should_appear(self, expected_text):
        assert (
            self.result.text == expected_text
        ), f'If button was clicked, there should be {expected_text}"'
