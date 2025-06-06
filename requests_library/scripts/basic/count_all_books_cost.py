from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/4.3/5/index.html')

if html_data:
    html = BeautifulSoup(html_data, 'lxml')
    prices = [
        float(price.text.split(':')[1].strip('$ '))
        for price in html.select('.price')
    ]
    amount = [
        int(count.text.rsplit(':')[1].strip())
        for count in html.select('.stock')
    ]
    total_cost = sum([price * amount for price, amount in zip(prices, amount)])
    print(f'Total cost of all books: ${total_cost:.2f}')
else:
    print('The page is unavailable')
