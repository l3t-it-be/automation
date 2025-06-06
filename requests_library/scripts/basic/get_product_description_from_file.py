from bs4 import BeautifulSoup

with open('files/htmls/iphone15.html', encoding='utf-8') as product_file:
    html = BeautifulSoup(product_file, 'lxml')
    print(html.select_one('p.card-description').text)
