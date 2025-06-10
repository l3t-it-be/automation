from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless mode
    browser.get('https://parsinger.ru/selenium/9/9.4.3/index.html')

    browser.find_element('xpath', '//a[text()="Правильный путь"]').click()

    WebDriverWait(browser, 6).until(
        ec.url_to_be(
            'https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure'
        )
    )

    password = browser.find_element('css selector', '#password').text
    print(password)
