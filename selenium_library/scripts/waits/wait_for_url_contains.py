from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get(
        'https://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html'
    )
    while True:
        search_button = browser.find_element('css selector', '#searchLink')
        search_button.click()

        try:
            WebDriverWait(browser, 5).until(ec.url_contains('qLChv49'))
            browser.find_element('css selector', '#checkButton').click()
            password = browser.find_element('css selector', 'p')
            print(password.text.split(':')[1].strip())
            break
        except TimeoutException:
            continue
