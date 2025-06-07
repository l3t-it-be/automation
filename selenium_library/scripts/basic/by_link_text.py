from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/2/2.html')
    browser.find_element('link text', '16243162441624').click()
    result = browser.find_element('css selector', '#result').text
    print(result)
