from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.3/index.html')

    for _ in range(4):
        iframe = browser.find_element('css selector', 'iframe')
        browser.switch_to.frame(iframe)
        browser.find_element('css selector', 'button.button').click()

    password = browser.find_element('css selector', '.password-container').text
    print(password)
