from selenium.webdriver import ActionChains, Keys

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.3/index.html')

    button = browser.find_element('css selector', '#instructions')

    actions = ActionChains(browser)
    actions.key_down(Keys.CONTROL, button).key_down(Keys.ALT).key_down(
        Keys.SHIFT
    ).send_keys('T').key_up(Keys.CONTROL).key_up(Keys.ALT).key_up(
        Keys.SHIFT
    ).perform()

    access_code = browser.find_element(
        'css selector', '[key="access_code"]'
    ).text
    print(access_code)
