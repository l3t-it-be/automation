from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.5.3/index.html')

    browser.find_element('css selector', '#showProducts').click()

    products = WebDriverWait(browser, 10).until(
        ec.visibility_of_all_elements_located(('css selector', '.product'))
    )

    prices = browser.find_elements('css selector', '.price')
    prices_lst = []
    for price in prices:
        browser.execute_script(
            'return arguments[0].scrollIntoView(true);', price
        )
        prices_lst.append(int(price.text.strip('$')))

    input_field = browser.find_element('css selector', '#sumInput')
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', input_field
    )
    input_field.send_keys(sum(prices_lst))
    browser.find_element('css selector', '#checkSum').click()

    password = WebDriverWait(browser, 2).until(
        ec.visibility_of_element_located(('css selector', '#secretMessage'))
    )
    print(password.text)
