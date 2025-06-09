from datetime import datetime

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/methods/5/index.html')

    urls = [
        element.get_attribute('href')
        for element in browser.find_elements('css selector', 'a[href]')
    ]

    max_date = None
    the_very_url = None
    result = None
    for url in urls:
        browser.get(url)
        cookies = browser.get_cookies()

        for cookie in cookies:
            expiry_date = datetime.fromtimestamp(cookie['expiry'])
            if max_date is None or expiry_date > max_date:
                max_date = expiry_date
                the_very_url = url
                result = browser.find_element('css selector', '#result').text

    print(
        f'Самый долгий срок действия: {max_date} у cookie на странице {the_very_url}',
        result,
        sep='\n',
    )
