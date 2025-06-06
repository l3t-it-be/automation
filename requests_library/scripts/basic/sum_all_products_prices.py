from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/4.1/1/index4.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    print(
        sum(
            [
                int(price.text.rsplit(' ', 1)[0].replace(' ', ''))
                for price in html.select('.product_price')
            ]
        )
    )
else:
    print('The page is unavailable')
