from selenium.webdriver import ActionChains

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.2/index.html')

    element = browser.find_element('css selector', '#dblclick-area')

    action = ActionChains(browser)
    action.double_click(element).perform()

    password = browser.find_element('css selector', '#password').text
    print(password)
