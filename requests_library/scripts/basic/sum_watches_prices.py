from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/html/index1_page_1.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    watches_total_cost = sum(
        [int(price.text.split()[0].strip()) for price in html.select('.price')]
    )
    print(f'All watches total cost: {watches_total_cost}')
else:
    print('The page is unavailable')
