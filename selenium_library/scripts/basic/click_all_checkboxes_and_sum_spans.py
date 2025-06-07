from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/scroll/2/index.html')

    numbers = []
    for item in browser.find_elements('css selector', 'div.item'):
        checkbox = item.find_element('css selector', 'input[type="checkbox"]')
        checkbox.click()
        span_text = item.find_element('css selector', 'span').text
        if span_text.isdigit():
            numbers.append(int(span_text))

    print(sum(numbers))
