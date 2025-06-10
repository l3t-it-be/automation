from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/8/8.2.2/index.html')

    window_width = browser.get_window_size()['width']
    window_height = browser.get_window_size()['height']

    browser.find_element('css selector', 'input#answer').send_keys(
        window_width + window_height
    )
    browser.find_element('css selector', 'button#checkBtn').click()

    password = browser.find_element('css selector', '#resultMessage')
    print(password.text.split()[1].strip())
