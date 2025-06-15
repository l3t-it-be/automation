import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.2/index.html')

    browser.find_element('css selector', '#startButton').click()

    numbers = []
    while not 'index_2' in browser.current_url:
        try:
            if WebDriverWait(browser, 5).until(
                ec.url_matches(
                    r'^https://parsinger\.ru/selenium/9/9\.4\.2/ok/ok_\d+\.html$'
                )
            ):
                number = browser.find_element('css selector', '.number').text
                numbers.append(int(number))
                time.sleep(1)
        except TimeoutException:
            break

    browser.find_element('css selector', '#sumInput').send_keys(sum(numbers))
    browser.find_element('css selector', '#checkButton').click()
    password = browser.find_element('css selector', '#result')
    print(password.text.split(':')[1].strip())
