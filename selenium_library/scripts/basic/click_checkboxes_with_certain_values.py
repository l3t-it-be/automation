from selenium_library.browser_setup import browser

with browser:
    with open('files/text_files/numbers.txt') as numbers_file:
        content = numbers_file.read()
        numbers = [
            int(num.strip())
            for num in content.split(',')
            if num.strip().isdigit()
        ]

    browser.get('https://parsinger.ru/selenium/5/5.html')
    checkboxes = [
        el
        for el in browser.find_elements('css selector', 'input.check')
        if int(el.get_attribute('value')) in numbers
    ]
    for checkbox in checkboxes:
        checkbox.click()

    browser.find_element('css selector', 'input.btn').click()
    result = browser.find_element('css selector', '#result').text
    print(result)
