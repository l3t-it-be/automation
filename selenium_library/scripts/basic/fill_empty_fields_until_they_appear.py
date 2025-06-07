from selenium.webdriver import Keys

from selenium_library.browser_setup import browser, random_generator

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.2/index.html')

    while True:
        fields = browser.find_elements(
            'xpath', '//div[@data-filled="false"]/../input'
        )
        if not fields:
            break
        fields[0].send_keys(random_generator.word(), Keys.ENTER, Keys.DOWN)

    password = browser.find_element('css selector', '#hidden-password')
    print(password.text.split()[1].strip())
