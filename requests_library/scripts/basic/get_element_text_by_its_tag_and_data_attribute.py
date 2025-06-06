from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/4.1/1/index.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    print(html.select_one('li[data-key="cooling_system"]').text)
else:
    print('The page is unavailable')
