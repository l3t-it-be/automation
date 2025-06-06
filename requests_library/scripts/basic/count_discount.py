from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/html/hdd/4/4_1.html')

if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    current_price = int(html.select_one('#price').text.split()[0].strip())
    old_price = int(html.select_one('#old_price').text.split()[0].strip())
    discount = (old_price - current_price) * 100 / old_price
    print(f'{discount:.1f}%')
else:
    print('The page is unavailable')
