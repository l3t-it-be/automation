from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.2/index.html')

    browser.find_element('css selector', '#ask-jaskier').click()

    wait = WebDriverWait(browser, 15, poll_frequency=1)

    wait.until(
        ec.text_to_be_present_in_element_value(
            ('css selector', '#recipe_field'), 'Селениумий'
        )
    )
    password = wait.until(
        ec.visibility_of_element_located(('css selector', '#password'))
    )
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', password
    )
    print(password.text)
