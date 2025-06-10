from selenium.webdriver import ActionChains

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/draganddrop/1/index.html')

    red = browser.find_element('css selector', '#field1')
    gray = browser.find_element('css selector', '#field2')

    action = ActionChains(browser)
    action.drag_and_drop(red, gray).perform()

    result = browser.find_element('css selector', '#result').text
    print(result)
