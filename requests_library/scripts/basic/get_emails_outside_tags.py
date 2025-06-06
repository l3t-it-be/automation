from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/4.1/1/index5.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    emails = [
        email.next_sibling.strip()
        for email in html.select('.email_field strong')
    ]
    print(emails)
else:
    print('The page is unavailable')
