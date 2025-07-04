import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.stepik.pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.text_in_url = 'profile'
        self.student_name_locator = ('css selector', 'h1')

    @allure.step('Assert Profile page has its text in URL')
    def should_be_profile_page(self):
        WebDriverWait(self.browser, 5).until(ec.url_contains(self.text_in_url))

    @property
    @allure.step('Actual student name')
    def student_name_actual(self):
        return self.find(self.student_name_locator)

    @allure.step('Assert student name actual matches the one expected')
    def student_name_should_match_the_one_authenticated(
        self, student_name_expected
    ):
        self.element_get_expected_text(
            self.student_name_actual, student_name_expected, 'Student Name'
        )
