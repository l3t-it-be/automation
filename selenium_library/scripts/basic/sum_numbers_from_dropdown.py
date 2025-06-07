from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')

    sum_numbers = sum(
        [
            int(num.text)
            for num in browser.find_elements('css selector', 'option')
        ]
    )

    browser.find_element('css selector', '#input_result').send_keys(
        sum_numbers
    )
    browser.find_element('css selector', 'input.btn').click()

    result = browser.find_element('css selector', '#result').text
    print(result)
