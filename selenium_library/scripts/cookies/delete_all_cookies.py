from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.2/index.html')

    browser.delete_all_cookies()
    password = browser.find_element('css selector', '#password')
    print(password.text.split()[1])
