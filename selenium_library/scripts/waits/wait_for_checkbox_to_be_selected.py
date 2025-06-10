from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.9/6/index.html')

    checkbox = browser.find_element('css selector', '#myCheckbox')
    WebDriverWait(browser, 5).until(ec.element_to_be_selected(checkbox))
    browser.find_element('css selector', 'button').click()

    result = browser.find_element('css selector', '#result').text
    print(result)
