from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.3/index.html')

    cookies = browser.get_cookies()

    song_name = None
    if len(cookies) == 1:
        song_name = cookies[0]['name']
        print(song_name)

    browser.find_element('css selector', '#phraseInput').send_keys(song_name)
    browser.find_element('css selector', '#checkButton').click()

    motto = browser.find_element('css selector', '#result').text
    print(motto)
