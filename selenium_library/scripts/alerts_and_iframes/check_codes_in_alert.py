from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')

    pins = browser.find_elements('css selector', 'span.pin')
    check_button = browser.find_element('css selector', '#check')

    for pin in pins:
        pin_code = pin.text
        check_button.click()

        alert = browser.switch_to.alert
        alert.send_keys(pin_code)
        alert.accept()

        result = browser.find_element('css selector', '#result').text
        if result != 'Неверный пин-код':
            print(result)
            break
