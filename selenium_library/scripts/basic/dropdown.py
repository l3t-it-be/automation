from selenium_library.browser_setup import browser

with browser:
    browser.get('https://suninjuly.github.io/selects1.html')

    num1 = int(browser.find_element('css selector', '#num1').text)
    num2 = int(browser.find_element('css selector', '#num2').text)
    result = num1 + num2

    browser.find_element('css selector', 'select').send_keys(result)
    browser.find_element('css selector', 'button').click()

    alert = browser.switch_to.alert
    code = alert.text.rsplit(' ', 1)[1]
    print(code)
    alert.accept()
