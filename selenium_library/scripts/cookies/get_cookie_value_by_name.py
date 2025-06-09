from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.1/index.html')
    print(browser.get_cookie('token_22')['value'])
