from selenium_library.browser_setup import browser

urls = [
    'https://fingerprint-scan.com',
    'https://bot.sannysoft.com/',
    'https://browserscan.net/bot-detection',
]

with browser:
    for url in urls:
        browser.get(url)
        if browser.execute_script('return navigator.webdriver'):
            print('You are detected')
        else:
            print('You are not detected')
