from bs4 import BeautifulSoup

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    html_data = browser.page_source
    html = BeautifulSoup(html_data, 'lxml')

    elements = html.select('span.num')
    formula = []

    for element in elements:
        formula.append(element.text.strip())
        next_sibling = element.next_sibling
        if next_sibling and next_sibling.strip():
            formula.append(next_sibling.strip())

    number = eval(' '.join(formula))
    browser.find_element('css selector', 'select').send_keys(str(number))

    browser.find_element('css selector', 'input.btn').click()
    result = browser.find_element('css selector', '#result').text
    print(result)
