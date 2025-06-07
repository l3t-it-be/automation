from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.1/')

    browser.switch_to.frame(browser.find_element('css selector', 'iframe'))
    text = browser.page_source

    letters = []

    words = text.split()
    for word in words:
        if '*' in word:
            for i in range(len(word)):
                if i != 0:
                    if word[i - 1] == '*':
                        if i != len(word) - 1:
                            if word[i + 1] == '*':
                                letters.append(word[i])

print(''.join(letters))
