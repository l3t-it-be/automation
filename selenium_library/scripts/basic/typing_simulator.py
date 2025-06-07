from selenium.webdriver import ActionChains, Keys

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.6/3/index.html')

    while True:
        current_char = browser.find_element(
            'css selector', '.current-char'
        ).text

        action = ActionChains(browser)
        if current_char == '⎵':
            action.send_keys(Keys.SPACE).perform()
        else:
            action.send_keys(current_char).perform()

        code = browser.find_element('css selector', '#secret-code').text
        if code:
            print(code)
            break
