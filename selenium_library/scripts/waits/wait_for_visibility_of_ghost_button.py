from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.5.2/index.html')

    WebDriverWait(browser, 5).until(
        ec.visibility_of_element_located(('css selector', '#ghost-button'))
    ).click()

    password = browser.find_element('css selector', '#password-display')
    print(password.text.split()[1].strip())
