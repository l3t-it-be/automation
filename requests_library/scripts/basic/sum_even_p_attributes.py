from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/4.3/4/index.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    sum_p_attrs = sum(
        [
            int(p['id']) + int(''.join(p['class']))
            for p in html.select('p')
            if len(p.text.replace(' ', '')) % 2 == 0
        ]
    )
    print(
        f'Sum of ID и CLASS attributes of <p> tags '
        f'with even text length without spaces: {sum_p_attrs}'
    )
else:
    print('The page is unavailable')
