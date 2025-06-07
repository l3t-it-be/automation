import time

from selenium_library.browser_setup import browser

url = 'https://2ip.ru/'
with browser:
    browser.get(url)

    my_ip = browser.find_element('css selector', '.ip span').text
    my_city_and_country = browser.find_element(
        'css selector', '#ip-info-city'
    ).text
    print(f'My IP: {my_ip}\nMy city and country: {my_city_and_country}')
