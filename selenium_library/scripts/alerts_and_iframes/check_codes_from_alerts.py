from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')

    buttons = browser.find_elements('css selector', 'input.buttons')
    input_field = browser.find_element('css selector', '#input')
    check_button = browser.find_element('css selector', '#check')

    for button in buttons:
        button.click()

        alert = browser.switch_to.alert
        alert_text = alert.text
        alert.accept()

        input_field.send_keys(alert_text)
        check_button.click()

        result = browser.find_element('css selector', '#result').text
        if result != 'Неверный пин-код':
            print(result)
            break
