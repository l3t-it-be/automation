from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/8/8.3.1/index.html')

    browser.find_element('css selector', '#alertButton').click()
    browser.switch_to.alert.accept()

    browser.find_element('css selector', '#promptButton').click()
    prompt = browser.switch_to.alert
    prompt.send_keys('Alert')
    prompt.accept()

    browser.find_element('css selector', '#confirmButton').click()
    browser.switch_to.alert.accept()

    password = WebDriverWait(browser, 5).until(
        ec.visibility_of_element_located(('css selector', '#secretKey'))
    )
    print(password.text.split()[1].strip())
