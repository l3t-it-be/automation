from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    result = sum(
        [
            int(cookie['value'])
            for cookie in browser.get_cookies()
            if int(cookie['name'].rsplit('_', 1)[1]) % 2 == 0
        ]
    )
    print(result)
