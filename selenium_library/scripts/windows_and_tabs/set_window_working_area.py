import time

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/window_size/1/')

    window_size = browser.get_window_size()
    width_border = window_size['width'] - browser.execute_script(
        'return window.innerWidth'
    )
    height_border = window_size['height'] - browser.execute_script(
        'return window.innerHeight'
    )

    browser.set_window_size(555 + width_border, 555 + height_border)
    time.sleep(0.5)

    result = browser.find_element('css selector', '#result')
    print(result.text)
