from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/table/3/index.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    sum_bold_numbers = sum(
        [float(number.text.strip()) for number in html.select('b')]
    )
    print(sum_bold_numbers)
else:
    print('The page is unavailable')
