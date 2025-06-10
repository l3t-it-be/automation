from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.1.1/index.html')

    buttons = browser.find_elements('css selector', '.button-container button')
    for button in buttons:
        WebDriverWait(browser, 15).until(ec.element_to_be_clickable(button))
        button.click()

    password = browser.find_element('css selector', '#message')
    print(password.text.split(':')[1].strip())
