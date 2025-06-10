import time

from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless mode
    browser.get('https://parsinger.ru/selenium/5.7/4/index.html')

    container = browser.find_element('css selector', '#main_container')
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

    checkboxes = browser.find_elements(
        'css selector', '.child_container input'
    )
    for checkbox in checkboxes:
        value = int(checkbox.get_attribute('value'))
        if value % 2 == 0:
            checkbox.click()

    button = browser.find_element('css selector', '.alert_button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

    alert = browser.switch_to.alert
    result = alert.text
    print(result)
    alert.accept()
