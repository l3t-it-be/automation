from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')

    browser.find_element('css selector', '#codeInput').send_keys('Дрогон')
    browser.find_element('css selector', '#clickButton').click()
    code = browser.find_element('css selector', '#codeOutput').text
    print(code)
