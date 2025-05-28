from selenium_library.browser_setup import browser

with browser:
    browser.get('https://suninjuly.github.io/huge_form.html')

    elements = browser.find_elements('css selector', 'input')
    phrase = 'Hello, World!'
    for element in elements:
        element.send_keys(phrase)
    browser.find_element('css selector', 'button.btn').click()

    alert = browser.switch_to.alert
    code = alert.text.rsplit(' ', 1)[1]
    print(code)
    alert.accept()
