import time

from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless mode
    browser.get('https://parsinger.ru/selenium/7/7.5/index.html')

    container = browser.find_element('css selector', '#container')
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

    numbers = []

    cards = container.find_elements('css selector', '.card')
    for card in cards:
        browser.execute_script(
            'return arguments[0].scrollIntoView(true);', card
        )
        like_button = card.find_element('css selector', '.like-btn')
        like_button.click()
        numbers.append(
            int(card.find_element('css selector', '.big-number').text)
        )

    print(sum(numbers))
