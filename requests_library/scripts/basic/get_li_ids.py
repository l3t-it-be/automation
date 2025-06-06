from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/4.1/1/index4.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    li_ids = [li['id'] for li in html.select('li[id]')]
    print('\n'.join(li_ids))
else:
    print('The page is unavailable')
