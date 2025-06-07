from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    while True:
        result = browser.find_element('css selector', '#result').text
        if result.isdigit():
            print(result)
            break
        browser.refresh()
