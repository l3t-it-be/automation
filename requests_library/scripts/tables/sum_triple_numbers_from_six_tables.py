from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/table/7/index.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    result = sum(
        [
            int(number.text.strip())
            for number in html.select('td')
            if int(number.text.strip()) % 3 == 0
        ]
    )
    print(result)
else:
    print('The page is unavailable')
