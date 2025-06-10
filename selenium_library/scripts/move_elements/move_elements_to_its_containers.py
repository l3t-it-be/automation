import time

from selenium.webdriver import ActionChains

from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless mode
    browser.get('https://parsinger.ru/selenium/5.10/8/index.html')
    balls = [
        browser.find_element('css selector', f'#piece_{i}')
        for i in range(100, 801, 100)
    ]
    containers = [
        browser.find_element('css selector', f'#range_{i}')
        for i in range(100, 801, 100)
    ]

    actions = ActionChains(browser)
    for ball, container in zip(balls, containers):
        actions.drag_and_drop(ball, container).perform()

    time.sleep(2)

    result = browser.find_element('css selector', '#message').text
    print(result)
