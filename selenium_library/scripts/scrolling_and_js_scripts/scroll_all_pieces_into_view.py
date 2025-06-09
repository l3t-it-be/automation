from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')

    pieces = browser.find_elements('css selector', 'button.clickMe')
    for piece in pieces:
        browser.execute_script(
            'return arguments[0].scrollIntoView(true);', piece
        )
        piece.click()

    alert = browser.switch_to.alert
    result = alert.text
    print(result)
    alert.accept()
