import time

from bs4 import BeautifulSoup

from selenium_library.browser_setup import browser
from selenium_library.scripts.solving_captcha.captcha_utils import (
    solve_yandex_captcha,
    results_dict,
    report_captcha_result,
)

with browser:
    url = 'https://captcha-parsinger.ru/yandex?page=3'
    browser.get(url)
    time.sleep(2)

    if 'Подтвердите, что вы не робот' in browser.page_source:
        solve_yandex_captcha()

    while True:
        page_data = BeautifulSoup(browser.page_source, 'lxml')
        articles = [
            int(article.text.split(':')[1].strip())
            for article in page_data.select('ul li:nth-child(1)')
        ]

        if articles:
            if 'captchaId' in results_dict:
                report_captcha_result(results_dict['captchaId'], True)

            articles_sum = sum(articles)
            print(f'Articles sum on page {url}: {articles_sum}')
            break

        else:
            if 'captchaId' in results_dict:
                report_captcha_result(results_dict['captchaId'], False)

            print(f'No articles found, retrying...')
            solve_yandex_captcha()
