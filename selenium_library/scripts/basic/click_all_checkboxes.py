from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')
    checkboxes = [
        el for el in browser.find_elements('css selector', 'input.check')
    ]
    for checkbox in checkboxes:
        checkbox.click()

    browser.execute_script('window.scrollBy(0, 50);')
    browser.find_element('css selector', 'input.btn').click()
    result = browser.find_element('css selector', '#result').text
    print(result)
