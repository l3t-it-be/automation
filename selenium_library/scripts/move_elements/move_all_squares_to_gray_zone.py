from selenium.webdriver import ActionChains

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.10/2/index.html')
    green_squares = browser.find_elements('css selector', '.draganddrop')
    gray_zone = browser.find_element('css selector', '.draganddrop_end')
    action = ActionChains(browser)

    for square in green_squares:
        action.drag_and_drop(square, gray_zone).perform()

    result = browser.find_element('css selector', '#message').text
    print(result)
