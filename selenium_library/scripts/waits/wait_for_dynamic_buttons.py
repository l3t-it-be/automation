from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.3.1/index.html')

    wait = WebDriverWait(browser, 15, poll_frequency=1)

    start_button = browser.find_element('css selector', '#startButton')
    wait.until(ec.element_to_be_clickable(start_button)).click()

    for _ in range(5):
        wait.until(
            ec.element_to_be_clickable(('css selector', '#dynamicButton'))
        ).click()

    password = browser.find_element('css selector', '#secretPassword')
    print(password.text.split()[1].strip())
