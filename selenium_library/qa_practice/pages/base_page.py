class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.result_locator = ('css selector', '#result-text')

    def open_page(self, url):
        self.browser.set_window_size(1920, 1080)
        self.browser.get(url)
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
