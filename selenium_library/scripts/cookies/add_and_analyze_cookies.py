import ast
import time

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.6/1/index.html')
    browser.delete_all_cookies()
    browser.refresh()

    min_age = float('inf')
    max_number_of_skills = -float('inf')
    the_very_cookie = None

    with open(
        'files/text_files/cookies.txt', encoding='utf-8'
    ) as cookies_file:
        cookies_content = cookies_file.read()
        cookies = ast.literal_eval(cookies_content)
        for cookie in cookies:
            browser.add_cookie(cookie)
            browser.refresh()
            time.sleep(0.5)

            age = int(
                browser.find_element('css selector', '#age')
                .text.split()[1]
                .strip()
            )
            number_of_skills = len(
                browser.find_elements('css selector', '#skillsList li')
            )
            if age < min_age and number_of_skills > max_number_of_skills:
                min_age = age
                max_number_of_skills = number_of_skills
                the_very_cookie = cookie

            browser.delete_all_cookies()
            browser.refresh()

    print(
        f'Cookie: {the_very_cookie}\nAge: {min_age}, Number of Skills: {max_number_of_skills}'
    )
