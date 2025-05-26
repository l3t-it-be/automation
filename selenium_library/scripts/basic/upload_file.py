import os

from selenium.webdriver.common.by import By

from selenium_library.browser_setup import browser, random_generator

with browser:
    browser.get('https://suninjuly.github.io/file_input.html')

    browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys(
        random_generator.first_name()
    )
    browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]').send_keys(
        random_generator.last_name()
    )
    browser.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys(
        random_generator.email()
    )

    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(
        os.path.abspath('files/text_files/hello_world.txt')
    )
    browser.find_element(By.CSS_SELECTOR, 'button').click()

    alert = browser.switch_to.alert
    code = alert.text.rsplit(' ', 1)[1]
    print(code)
    alert.accept()
