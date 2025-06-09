import time

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')

    container = browser.find_element('css selector', '#scroll-container')
    last_height = browser.execute_script(
        'return arguments[0].scrollHeight', container
    )

    while True:
        browser.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollHeight', container
        )
        time.sleep(0.5)

        new_height = browser.execute_script(
            'return arguments[0].scrollHeight', container
        )

        if new_height == last_height:
            break
        last_height = new_height

    result = sum(
        [
            int(p.text)
            for p in browser.find_elements('css selector', 'p')
            if p.text.isdigit()
        ]
    )
    print(result)
