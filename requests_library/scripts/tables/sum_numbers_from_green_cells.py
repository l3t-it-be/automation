from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/table/4/index.html')
if html_data:
    html = BeautifulSoup(html_data, 'html.parser')
    green_cells_numbers_sum = sum(
        [float(number.text.strip()) for number in html.select('.green')]
    )
    print(f'{green_cells_numbers_sum:.13f}')
else:
    print('The page is unavailable')
