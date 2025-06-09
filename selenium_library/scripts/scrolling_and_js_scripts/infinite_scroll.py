from selenium.webdriver import Keys

from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless option
    browser.get('https://parsinger.ru/infiniti_scroll_1/')

    scrolling_container = browser.find_element(
        'css selector', '#scroll-container'
    )

    data = []
    numbers = []

    while True:
        number_elements = scrolling_container.find_elements(
            'css selector', 'span'
        )
        for element in number_elements:
            if element not in data:
                element.find_element('css selector', 'input').send_keys(
                    Keys.DOWN
                )
                data.append(element)
                numbers.append(int(element.text))
            if element.get_attribute('class') == 'last-of-list':
                break
        else:
            continue
        break

    print(sum(numbers))
