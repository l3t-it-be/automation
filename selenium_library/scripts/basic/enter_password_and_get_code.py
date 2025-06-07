from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')

    browser.find_element('css selector', '#showTextBtn').click()
    password = browser.find_element('css selector', '#text1').text
    browser.find_element('css selector', '#userInput').send_keys(password)

    browser.find_element('css selector', '#checkBtn').click()
    code = browser.find_element('css selector', '#text2').text
    print(code)
