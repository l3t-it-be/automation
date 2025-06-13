from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/expectations/3/index.html')

    wait = WebDriverWait(browser, 20, poll_frequency=1)

    button = browser.find_element('css selector', 'button')
    wait.until(ec.element_to_be_clickable(button))
    button.click()

    wait.until(ec.title_is('345FDG3245SFD'))
    result = browser.find_element('css selector', '#result').text
    print(result)
