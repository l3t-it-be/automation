from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.5/index.html')

    button = browser.find_element('css selector', '#target')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

    secret_key = browser.find_element('css selector', '#secret-key')
    print(secret_key.text.split(':')[1].strip())
