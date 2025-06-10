from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.5.1/index.html')

    locator = ('css selector', '#order-number')
    order = WebDriverWait(browser, 15).until(
        ec.presence_of_element_located(locator)
    )
    print(order.text)
