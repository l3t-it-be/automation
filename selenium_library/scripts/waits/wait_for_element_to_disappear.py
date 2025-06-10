from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser, random_generator

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.7.1/index.html')

    browser.find_element('css selector', '#address').send_keys(
        random_generator.address()
    )
    dropdown = Select(browser.find_element('css selector', 'select'))
    dropdown.select_by_value('card')

    browser.find_element('css selector', '#submit-order').click()
    WebDriverWait(browser, 7).until(
        ec.invisibility_of_element_located(('css selector', '#spinner'))
    )

    WebDriverWait(browser, 2).until(
        ec.element_to_be_clickable(('css selector', '#confirm-address'))
    ).click()
    WebDriverWait(browser, 4).until(
        ec.invisibility_of_element_located(('css selector', '.modal'))
    )

    browser.find_element('css selector', '#get-code').click()
    password = browser.find_element('css selector', '#result')
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', password
    )
    print(password.text)
