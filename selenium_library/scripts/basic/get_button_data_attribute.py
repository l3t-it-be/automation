from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
    button = browser.find_element('css selector', '#secret-key-button')
    button.click()
    print(button.get_attribute('data'))
