from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/4.1/1/index2.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    print(
        html.select_one(
            '.description_detail.class1.class2.class3'
            '[data-fdg45="value13"]'
            '[data-54dfg60="value14"]'
            '[data-d6f50hg="value15"]'
        ).text
    )
else:
    print('The page is unavailable')
