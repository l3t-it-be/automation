import time

from selenium.webdriver import ActionChains, Keys

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.5/index.html')

    containers = browser.find_elements(
        'css selector', '#containers-wrapper .scroll-container'
    )
    statuses = browser.find_elements('css selector', '.status')

    actions = ActionChains(browser)
    for container, status in zip(containers, statuses):
        actions.click(container).send_keys(Keys.END).perform()
        time.sleep(0.5)
        assert status.text == 'Прокручено!', f'Ошибка: {status.text}'

    access_code = browser.find_element('css selector', '[key="access_code"]')
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', access_code
    )
    print(access_code.text)
