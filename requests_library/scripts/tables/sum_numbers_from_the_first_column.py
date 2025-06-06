from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/table/2/index.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    first_column_numbers = [
        float(number.text.strip())
        for number in html.select('td:nth-of-type(1)')
    ]
    print(sum(first_column_numbers))
else:
    print('The page is unavailable')
