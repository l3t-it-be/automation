from selenium_library.browser_setup import browser

with browser:
    numbers = []
    for i in range(1, 7):
        url = f'https://parsinger.ru/blank/1/{i}.html'
        browser.get(url)

        browser.find_element('css selector', 'input[type="checkbox"]').click()
        num = int(browser.find_element('css selector', '#result').text)
        num_sqrt = num**0.5
        numbers.append(num_sqrt)

    print(round(sum(numbers), 9))
