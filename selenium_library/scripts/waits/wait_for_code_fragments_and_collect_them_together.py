from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

full_code = []
with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless mode
    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')

    elements = browser.find_elements('css selector', 'div.box_button')
    for element in elements:
        element.click()
        browser.find_element('css selector', '#close_ad').click()

        WebDriverWait(browser, 10).until(lambda _: element.text.strip() != '')
        code = element.text.strip()
        full_code.append(code)

print('-'.join(full_code))
