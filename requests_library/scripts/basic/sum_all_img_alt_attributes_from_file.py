from bs4 import BeautifulSoup

with open(
    'files/htmls/products_cards.html', encoding='utf-8'
) as products_file:
    html = BeautifulSoup(products_file, 'lxml')
    sum_alts = sum(
        [
            int(img['alt'])
            for img in html.select('img[alt]')
            if img['alt'].isdigit()
        ]
    )
    print(f'Sum of alt attribute values of all img tags: {sum_alts}')
