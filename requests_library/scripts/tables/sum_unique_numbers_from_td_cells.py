from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/table/1/index.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    unique_tds_sum = sum(
        set([float(td.text.strip()) for td in html.select('td')])
    )
    print(f'{unique_tds_sum:.13f}')
else:
    print('The page is unavailable')
