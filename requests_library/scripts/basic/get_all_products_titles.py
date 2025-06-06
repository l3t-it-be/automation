from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/4.1/1/index4.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    titles = [
        product_name.text.strip()
        for product_name in html.select('.product_name')
    ]
    print('\n'.join(titles))
else:
    print('The page is unavailable')
