from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.9/2/index.html')

    magic_block = WebDriverWait(browser, 5, 0.01).until(
        ec.element_to_be_clickable(('css selector', '#qQm9y1rk'))
    )
    magic_block.click()

    alert = browser.switch_to.alert
    result = alert.text
    print(result)
    alert.accept()
