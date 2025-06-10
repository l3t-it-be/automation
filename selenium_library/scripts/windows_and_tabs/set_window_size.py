from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1200, 700)
    browser.get('https://parsinger.ru/selenium/8/8.2.1/index.html')

    browser.find_element('css selector', '#checkSizeBtn').click()
    message = browser.find_element('css selector', '#message').text
    assert message == 'Размеры корректны!', 'Неверный размер окна'

    code = browser.find_element('css selector', '#secret').text
    print(code)
