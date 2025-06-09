from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    result = sum(
        [
            int(cookie['value'])
            for cookie in browser.get_cookies()
            if cookie['name'].startswith('secret_cookie_')
        ]
    )
    print(result)
