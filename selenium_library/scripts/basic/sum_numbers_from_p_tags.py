from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')

    sum_numbers = sum(
        [
            int(p.text)
            for p in browser.find_elements('css selector', 'p')
            if p.text.isdigit()
        ]
    )
    print(sum_numbers)
