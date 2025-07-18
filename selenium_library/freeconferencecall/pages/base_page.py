import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

        self.url = 'https://www.freeconferencecall.com/'
        self.browser_title = 'Free Conference Call Services'
        self.log_in_button_locator = ('css selector', 'a[href="/login"]')

    @allure.step('Open page')
    def open_page(self, url):
        return self.browser.get(url)

    @allure.step('Find element on page')
    def find(self, args):
        return self.browser.find_element(*args)

    @allure.step('Assert url contains text')
    def url_should_contain_text(self, text: str):
        assert text in self.browser.current_url, f'URL should contain {text}'

    @allure.step('Assert browser title contains text')
    def browser_title_should_contain_text(self, text):
        assert (
            text in self.browser.title
        ), f'Browser title should contain {text}'

    @staticmethod
    @allure.step('Assert element on page is visible and active')
    def element_is_visible_and_enabled(element, name):
        assert element.is_displayed(), f'{name} should be displayed'
        assert element.is_enabled(), f'{name} should be enabled'

    @staticmethod
    @allure.step('Get element text max length')
    def element_max_length(element):
        return int(element.get_attribute('maxlength'))

    @staticmethod
    @allure.step('Get element value attribute')
    def element_value(element):
        return element.get_attribute('value')

    @allure.step('Open Main page')
    def open_main_page(self):
        self.open_page(self.url)
        WebDriverWait(self.browser, 5).until(
            ec.title_contains(self.browser_title)
        )
        self.url_should_contain_text(self.url)
        self.browser_title_should_contain_text(self.browser_title)

    @property
    @allure.step('Log In button')
    def log_in_button(self):
        return self.find(self.log_in_button_locator)

    @allure.step('Open Login page')
    def open_login_page(self):
        self.element_is_visible_and_enabled(
            self.log_in_button, 'Log in button'
        )
        self.log_in_button.click()
