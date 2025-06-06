from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/4.1/1/index6.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    print(html.select_one('#section3 .section-text').next_sibling.strip())
else:
    print('The page is unavailable')
