import time

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/infiniti_scroll_3/')
    numbers = []

    for i in range(1, 6):
        container = browser.find_element(
            'css selector', f'#scroll-container_{i}'
        )
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

        spans = container.find_elements('css selector', 'span')
        nums = [int(span.text) for span in spans if span.text.isdigit()]
        numbers.extend(nums)

    print(sum(numbers))
