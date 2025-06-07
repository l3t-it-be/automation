from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')

    containers = browser.find_elements('css selector', '#main-container>div')

    for container in containers:
        color_code = container.find_element('css selector', 'span').text
        container.find_element('css selector', 'select').send_keys(color_code)
        container.find_element(
            'css selector', f'button[data-hex="{color_code}"]'
        ).click()
        container.find_element(
            'css selector', 'input[type="checkbox"]'
        ).click()
        container.find_element('css selector', 'input[type="text"]').send_keys(
            color_code
        )
        container.find_element('xpath', '//button[text()="Проверить"]').click()

    browser.find_element(
        'xpath', '//button[text()="Проверить все элементы"]'
    ).click()

    alert = browser.switch_to.alert
    result = alert.text
    print(result)
    alert.accept()
