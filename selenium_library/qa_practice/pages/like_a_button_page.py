from selenium.webdriver.common.by import By

from selenium_library.qa_practice.pages.base_page import BasePage


class LikeAButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.url = 'https://www.qa-practice.com/elements/button/like_a_button'
        self.like_a_button_locator = (By.LINK_TEXT, 'Click')

    @property
    def like_a_button(self):
        return self.find(self.like_a_button_locator)
