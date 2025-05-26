from selenium.webdriver.common.by import By

from selenium_library.browser_setup import browser, random_generator

with browser:
    browser.get('https://suninjuly.github.io/find_xpath_form')

    browser.find_element(By.XPATH, '//input[@name="first_name"]').send_keys(
        random_generator.first_name()
    )
    browser.find_element(By.XPATH, '//input[@name="last_name"]').send_keys(
        random_generator.last_name()
    )
    browser.find_element(
        By.XPATH, '//input[@class="form-control city"]'
    ).send_keys(random_generator.city())
    browser.find_element(By.XPATH, '//input[@id="country"]').send_keys(
        random_generator.country()
    )
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

    alert = browser.switch_to.alert
    code = alert.text.rsplit(' ', 1)[1]
    print(code)
    alert.accept()
