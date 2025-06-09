from selenium.webdriver import ActionChains

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.1/index.html')

    piter_griffin = browser.find_element('css selector', '#draggable')
    swimming_pool = browser.find_element('css selector', '#target')

    action = ActionChains(browser)
    action.drag_and_drop(piter_griffin, swimming_pool).perform()

    password = browser.find_element('css selector', '#password').text
    print(password)
