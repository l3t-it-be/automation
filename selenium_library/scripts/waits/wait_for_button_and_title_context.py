from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/expectations/4/index.html')

    wait = WebDriverWait(browser, 20, poll_frequency=1)

    button = browser.find_element('css selector', 'button')
    wait.until(ec.element_to_be_clickable(button))
    button.click()

    if wait.until(ec.title_contains('JK8HQ')):
        result = browser.title
    print(result)
