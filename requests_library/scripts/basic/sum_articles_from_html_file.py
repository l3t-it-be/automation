from bs4 import BeautifulSoup

with open('files/htmls/products.html', encoding='utf-8') as products_file:
    html = BeautifulSoup(products_file, 'lxml')
    sum_articuls = sum(
        [
            int(article.text.split()[1].strip())
            for article in html.select('p.card-articul')
        ]
    )
    print(f'Sum articles: {sum_articuls}')
