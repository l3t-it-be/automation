import time

from selenium_library.browser_setup import browser
from selenium_library.scripts.solving_captcha.captcha_utils import (
    solve_captcha,
    results_dict,
    report_captcha_result,
)
from selenium_library.useful_functions import get_articles_from_page

with browser:
    url = 'https://captcha-parsinger.ru/?page=3'
    browser.get(url)
    time.sleep(2)

    if 'Подтвердите, что вы не робот' in browser.page_source:
        solve_captcha('img')

    while True:
        articles = get_articles_from_page(browser)

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
            solve_captcha('img')
