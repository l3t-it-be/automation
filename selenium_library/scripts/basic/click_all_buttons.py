from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.2/index.html')

    buttons = [
        button for button in browser.find_elements('css selector', '.button')
    ]
    for button in buttons:
        button.click()

    print(browser.find_element('css selector', 'password').text)
