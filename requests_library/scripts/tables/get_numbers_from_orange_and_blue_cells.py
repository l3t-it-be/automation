from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/table/5/index.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    orange_numbers = [
        float(number.text.strip()) for number in html.select('.orange')
    ]
    blue_numbers = [
        float(number.text.strip()) for number in html.select('td:last-of-type')
    ]
    result = sum(
        [
            orange_num * blue_num
            for orange_num, blue_num in zip(orange_numbers, blue_numbers)
        ]
    )
    print(f'{result:.10f}')
else:
    print('The page is unavailable')
