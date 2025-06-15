from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.1/index.html')

    page_height = browser.execute_script('return document.body.scrollHeight')
    browser.execute_script(f'window.scrollTo(0, {page_height})')

    password = browser.find_element('css selector', '#secret-container')
    WebDriverWait(browser, 5).until(lambda _: password.text.strip() != '')
    print(password.text.split()[1].strip())
