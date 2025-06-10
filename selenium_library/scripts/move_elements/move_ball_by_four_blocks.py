from selenium.webdriver import ActionChains

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/draganddrop/2/index.html')

    ball = browser.find_element('css selector', '#draggable')
    blocks = browser.find_elements('css selector', '.box')

    action = ActionChains(browser)
    for block in blocks:
        action.drag_and_drop(ball, block).perform()

    result = browser.find_element('css selector', '#message').text
    print(result)
