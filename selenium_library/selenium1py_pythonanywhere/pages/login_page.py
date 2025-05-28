from selenium_library.selenium1py_pythonanywhere.pages.base_page import (
    BasePage,
)


class LoginPage(BasePage):
    def __init__(self, browser):
        self.browser = browser
        super().__init__(browser)

        self.text_in_url = 'login'
        self.login_form_locator = ('css selector', '#login_form')
        self.register_form_locator = ('css selector', '#register_form')

        self.registration_email_input_locator = (
            'css selector',
            '#id_registration-email',
        )
        self.registration_password_input_locator = (
            'css selector',
            '#id_registration-password1',
        )
        self.registration_confirm_password_input_locator = (
            'css selector',
            '#id_registration-password2',
        )
        self.submit_registration_button_locator = (
            'css selector',
            'button[name="registration_submit"]',
        )

    def should_be_login_page(self):
        self.url_should_contain_text(self.text_in_url)

    def should_have_login_form(self):
        assert self.find(
            self.login_form_locator
        ).is_displayed(), 'Login form is not presented'

    def should_have_register_form(self):
        assert self.find(
            self.register_form_locator
        ).is_displayed(), 'Register form is not presented'

    def should_be_on_login_page(self):
        self.should_be_login_page()
        self.should_have_login_form()
        self.should_have_register_form()

    def register_new_user(self, email, password):
        self.browser.execute_script('window.scrollBy(0, 100);')

        self.find(self.registration_email_input_locator).send_keys(email)
        self.find(self.registration_password_input_locator).send_keys(password)
        self.find(self.registration_confirm_password_input_locator).send_keys(
            password
        )
        self.find(self.submit_registration_button_locator).click()
