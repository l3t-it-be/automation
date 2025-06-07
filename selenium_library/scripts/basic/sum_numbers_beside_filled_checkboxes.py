from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')

    pairs_of_elements = browser.find_elements('css selector', '.parent')
    result = sum(
        [
            int(pair.find_element('css selector', 'textarea').text)
            for pair in pairs_of_elements
            if pair.find_element('css selector', '.checkbox').is_selected()
        ]
    )
    print(result)
