from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.1/index.html')

    WebDriverWait(browser, 40).until(
        ec.text_to_be_present_in_element(
            ('css selector', '#usd-rate'), '75.50 ₽'
        )
    )
    secret_code = WebDriverWait(browser, 2).until(
        ec.visibility_of_element_located(('css selector', '#secret-code'))
    )
    print(secret_code.text)
