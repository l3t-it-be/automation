from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/table/8/index.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    result = sum(
        [
            int(cell.text.strip())
            for cell in html.select('[colspan]')
            if cell.text.isdigit()
        ]
    )
    print(result)
else:
    print('The page is unavailable')
