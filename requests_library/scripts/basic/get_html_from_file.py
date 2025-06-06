from bs4 import BeautifulSoup

with open('files/htmls/index.html', encoding='utf-8') as html_file:
    html = BeautifulSoup(html_file, 'lxml')
    print(html)
