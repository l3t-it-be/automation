from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.3/index.html')

    wait = WebDriverWait(browser, 20, poll_frequency=1)

    locator = ('css selector', '#main-image')
    wait.until(
        ec.text_to_be_present_in_element_attribute(locator, 'src', 'success')
    )
    browser.find_element(*locator).click()

    code = wait.until(
        ec.visibility_of_element_located(('css selector', '#password'))
    ).text
    print(code)
