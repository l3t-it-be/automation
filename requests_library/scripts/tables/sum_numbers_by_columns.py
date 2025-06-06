from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/table/5/index.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')

    headers = [header.text.strip() for header in html.select('th')]
    numbers_by_rows = [
        [float(number.text.strip()) for number in row.select('td')]
        for row in html.select('tr')[1:]
    ]
    numbers_by_columns = list(zip(*numbers_by_rows))
    sum_numbers_by_columns = [sum(numbers) for numbers in numbers_by_columns]

    result = {
        header: round(sum_numbers, 3)
        for header, sum_numbers in zip(headers, sum_numbers_by_columns)
    }
    print(result)
else:
    print('The page is unavailable')
