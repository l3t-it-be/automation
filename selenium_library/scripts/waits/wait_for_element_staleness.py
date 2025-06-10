from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.7.2/index.html')

    browser.find_element('css selector', 'input.search-box').send_keys(
        'Selenium'
    )
    browser.find_element('css selector', '#search-button').click()

    old_result = browser.find_element('css selector', '#old-result')
    WebDriverWait(browser, 5).until(ec.staleness_of(old_result))

    browser.find_element('css selector', '#secret-button').click()
    password = browser.find_element('css selector', '#result').text
    print(password)
