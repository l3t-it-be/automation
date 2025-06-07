from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless option
    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')

    fields = browser.find_elements('css selector', '.text-field')
    for field in fields:
        field.clear()

    browser.find_element('css selector', '#checkButton').click()

    alert = browser.switch_to.alert
    result = alert.text
    print(result)
    alert.accept()
