from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.4/index.html')

    locator = ('css selector', '#booking-number')
    WebDriverWait(browser, 20).until(
        ec.element_attribute_to_include(locator, 'confirmed')
    )
    booking_number = browser.find_element(*locator).text

    browser.find_element('css selector', '#booking-input').send_keys(
        booking_number
    )
    browser.find_element('css selector', '#check-button').click()

    password = browser.find_element('css selector', '.password-value')
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', password
    )
    print(password.text)
