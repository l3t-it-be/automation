import math

import allure
from selenium.common import (
    TimeoutException,
    NoAlertPresentException,
)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

        self.url = 'https://selenium1py.pythonanywhere.com/'
        self.basket_link_locator = ('css selector', '.basket-mini a.btn')
        self.login_link_locator = ('css selector', '#login_link')
        self.search_button_locator = ('css selector', 'input.btn')

        self.user_icon = ('css selector', '.icon-user')
        self.user_email = ('css selector', 'tr:nth-child(2) td')

    @allure.step('Open page')
    def open_page(self, url):
        return self.browser.get(url)

    @allure.step('Find element')
    def find(self, args):
        return self.browser.find_element(*args)

    @staticmethod
    @allure.step('Assert element is visible and active')
    def element_is_visible_and_enabled(element, name):
        assert element.is_displayed(), f'{name} should be displayed'
        assert element.is_enabled(), f'{name} should be enabled'

    @staticmethod
    @allure.step('Assert element text matches the one expected')
    def element_get_expected_text(element, expected_text, name):
        assert (
            element.text == expected_text
        ), f'{name} should have text "{expected_text}", but got "{element.text} instead"'

    @property
    @allure.step('Basket link')
    def basket_link(self):
        return self.find(self.basket_link_locator)

    @allure.step('Assert basket link is visible and clickable')
    def basket_link_is_visible_and_clickable(self):
        self.element_is_visible_and_enabled(self.basket_link, 'Basket link')

    @property
    @allure.step('Login link')
    def login_link(self):
        return self.find(self.login_link_locator)

    @allure.step('Assert login link is visible and clickable')
    def login_link_is_visible_and_clickable(self):
        self.element_is_visible_and_enabled(self.login_link, 'Login link')

    @property
    @allure.step('Search button')
    def search_button(self):
        return self.find(self.search_button_locator)

    @allure.step('Assert search button is visible and clickable')
    def search_button_is_visible_and_clickable(self):
        self.element_is_visible_and_enabled(
            self.search_button, 'Search button'
        )

    @allure.step('Assert URL contains expected text')
    def url_should_contain_text(self, text: str):
        assert text in self.browser.current_url, f'url should contain {text}'

    @allure.step('Assert element is not displayed after 10 seconds')
    def element_is_not_present(self, selector, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                ec.presence_of_element_located(selector)
            )
        except TimeoutException:
            return True

        return False

    @allure.step(
        'Assert user email matches the one typed into registration form'
    )
    def should_be_authorized_user(self, email):
        self.find(self.user_icon).click()
        user_email = self.find(self.user_email)
        assert (
            user_email.text == email
        ), 'User email is not presented, probably unauthorised user'

    @allure.step('Solve quiz and type result into alert')
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            code = alert.text.rsplit(' ', 1)[-1].strip()
            print(f'Your code: {code}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')
