from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/blank/3/index.html')

    buttons = browser.find_elements('css selector', 'input.buttons')
    for button in buttons:
        button.click()

    titles = []
    tabs = browser.window_handles
    for tab in tabs:
        browser.switch_to.window(tab)
        title = browser.title
        if title.isdigit():
            titles.append(int(title))

    print(sum(titles))
