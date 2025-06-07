from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')

    buttons = browser.find_elements('css selector', 'input')
    for button in buttons:
        button.click()
        alert = browser.switch_to.alert
        alert.accept()

        result = browser.find_element('css selector', 'p#result').text
        if result:
            print(result)
            break
