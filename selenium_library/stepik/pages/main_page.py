from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.stepik.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.profile_menu_button_locator = (
            'css selector',
            'button[aria-label="Profile"]',
        )
        self.profile_button_locator = (
            'css selector',
            '[data-qa="menu-item-profile"]',
        )

    @property
    def profile_menu_button(self):
        return WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(self.profile_menu_button_locator)
        )

    @property
    def profile_button(self):
        return WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(self.profile_button_locator)
        )
