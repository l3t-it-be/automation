from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.4.1/index.html')

    scroll_marker1 = browser.find_element(
        'css selector', '.scroll-marker.marker-1'
    )
    scroll_marker2 = browser.find_element(
        'css selector', '.scroll-marker.marker-2'
    )

    actions = ActionChains(browser)
    actions.move_to_element(scroll_marker1).scroll_by_amount(1, 300).perform()

    countdown_locator = ('css selector', '.countdown')
    WebDriverWait(browser, 3).until(
        ec.text_to_be_present_in_element(countdown_locator, 'Код')
    )
    element = browser.find_element(*countdown_locator)
    code = element.text.split()[1].strip()

    actions.move_to_element(scroll_marker2).scroll_by_amount(1, 300).perform()
    browser.find_element('css selector', 'input').send_keys(code)
    browser.find_element('css selector', 'button').click()

    password = browser.find_element('css selector', '#final-key')
    print(password.text.split(':')[1].strip())
