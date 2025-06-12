import time

from selenium_library.browser_setup import browser
from selenium_library.scripts.solving_captcha.captcha_utils import (
    solve_recaptcha,
)
from selenium_library.useful_functions import get_articles_from_page

urls = [f'https://captcha-parsinger.ru/v2?page={num}' for num in range(1, 7)]
all_articles = []

with browser:
    for url in urls:
        browser.get(url)
        time.sleep(2)

        if 'Подтвердите, что вы не робот' in browser.page_source:
            solve_recaptcha()

        while True:
            articles = get_articles_from_page(browser)

            if articles:
                articles_sum = sum(articles)
                print(f'Articles sum on page {url}: {articles_sum}')
                all_articles.append(articles_sum)
                break
            else:
                print(f'Unable to get products articles from page {url}')
                solve_recaptcha()

print(f'Total sum of articles: {sum(all_articles)}')
