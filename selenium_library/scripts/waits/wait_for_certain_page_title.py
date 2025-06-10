from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless mode
    browser.get('https://parsinger.ru/selenium/9/9.2.1/index.html')

    browser.find_element('css selector', '#startScan').click()
    WebDriverWait(browser, 25).until(ec.title_is('Access Granted'))

    password = browser.find_element('css selector', '#passwordValue')
    print(password.text.split(':')[1].strip())
