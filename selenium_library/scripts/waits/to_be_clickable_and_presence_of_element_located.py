from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless mode
    browser.get('https://parsinger.ru/expectations/6/index.html')

    wait = WebDriverWait(browser, 20, poll_frequency=1)

    button = wait.until(ec.element_to_be_clickable(('css selector', '#btn')))
    button.click()

    element = wait.until(
        ec.presence_of_element_located(('css selector', '.BMH21YY'))
    )
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', element
    )
    print(element.text)
