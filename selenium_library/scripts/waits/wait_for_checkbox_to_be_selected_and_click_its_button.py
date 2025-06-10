from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')

    checkboxes = browser.find_elements(
        'css selector', 'input[type="checkbox"]'
    )
    buttons = browser.find_elements('css selector', 'button')

    for checkbox, button in zip(checkboxes, buttons):
        WebDriverWait(browser, 10, 0.01).until(
            ec.element_to_be_selected(checkbox)
        )
        button.click()

    result = browser.find_element('css selector', '#result').text
    print(result)
