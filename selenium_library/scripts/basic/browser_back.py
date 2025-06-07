from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.2/index.html')

    browser.find_element('css selector', 'a[href]').click()
    browser.find_element('css selector', 'a[href]').click()
    browser.back()
    browser.back()

    browser.find_element('css selector', '#getPasswordBtn').click()
    alert = browser.switch_to.alert
    result = alert.text.split(':')[1].strip()
    print(result)
    alert.accept()
