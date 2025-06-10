from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/expectations/3/index.html')
    button = browser.find_element('css selector', 'button')
    WebDriverWait(browser, 3).until(ec.element_to_be_clickable(button))
    button.click()

    WebDriverWait(browser, 20).until(ec.title_is('345FDG3245SFD'))
    result = browser.find_element('css selector', '#result').text
    print(result)
