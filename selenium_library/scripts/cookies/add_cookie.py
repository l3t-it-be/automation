from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.3/index.html')

    browser.add_cookie({'name': 'secretKey', 'value': 'selenium123'})
    browser.refresh()

    password = browser.find_element('css selector', '#password')
    print(password.text.split()[1])
