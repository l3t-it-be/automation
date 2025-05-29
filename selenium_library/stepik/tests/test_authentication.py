import time

import pytest

from selenium_library.stepik.pages.login_page import LoginPage
from selenium_library.stepik.pages.main_page import MainPage
from selenium_library.stepik.pages.profile_page import ProfilePage
from selenium_library.stepik.test_data.credentials import student_name


@pytest.mark.stepik
@pytest.mark.login
@pytest.mark.regression
class TestStepik:
    @pytest.mark.smoke
    def test_successful_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open_page(login_page.url)
        time.sleep(2)

        login_page.log_in_button.click()
        login_page.fill_out_login_form()

        main_page = MainPage(browser)
        main_page.profile_menu_button.click()
        main_page.profile_button.click()

        profile_page = ProfilePage(browser)
        profile_page.should_be_profile_page()
        profile_page.student_name_should_match_the_one_authenticated(
            student_name
        )
