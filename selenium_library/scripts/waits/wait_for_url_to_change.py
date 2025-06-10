from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.4/index.html')

    browser.find_element('css selector', '.btn').click()

    current_url = browser.current_url
    WebDriverWait(browser, 5).until(ec.url_changes(current_url))

    password = browser.find_element('css selector', '#password')
    print(password.text.split(':')[1].strip())
