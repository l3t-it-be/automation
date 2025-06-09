from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/scroll/4/index.html')

    buttons = browser.find_elements('css selector', 'button.btn')
    nums = []

    for button in buttons:
        browser.execute_script(
            'return arguments[0].scrollIntoView(true);', button
        )
        button.click()
        num = int(
            browser.find_element('css selector', 'p#result').text.strip()
        )
        nums.append(num)

    print(sum(nums))
