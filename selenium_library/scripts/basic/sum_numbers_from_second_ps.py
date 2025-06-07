from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')

    sum_second_ps = sum(
        [
            int(p.text)
            for p in browser.find_elements(
                'xpath', '//div[@class="text"]/p[2]'
            )
            if p.text.isdigit()
        ]
    )
    print(sum_second_ps)
