from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless mode
    browser.get('https://parsinger.ru/selenium/9/9.7.3/index.html')

    browser.find_element('css selector', '#summonBtn').click()

    wait = WebDriverWait(browser, 10, poll_frequency=0.01)

    wait.until(ec.number_of_windows_to_be(5))
    windows = browser.window_handles
    browser.switch_to.window(windows[0])

    browser.find_element('css selector', '#passwordBtn').click()
    wait.until(ec.alert_is_present())

    alert = browser.switch_to.alert
    password = alert.text.split(':')[1].strip()
    print(password)
    alert.accept()
