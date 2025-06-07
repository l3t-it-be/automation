from selenium.webdriver import ActionChains

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.4/index.html')

    element = browser.find_element('css selector', '#context-area')
    action = ActionChains(browser)
    action.context_click(element).perform()

    browser.find_element(
        'css selector', '[data-action="get_password"]'
    ).click()

    password = browser.find_element('css selector', '[key="access_code"]').text
    print(password)
