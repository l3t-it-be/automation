from selenium.webdriver.common.by import By

from selenium_library.browser_setup import browser
from selenium_library.useful_functions import calculate_formula

with browser:
    browser.get('https://suninjuly.github.io/alert_accept.html')

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    browser.switch_to.alert.accept()

    formula = browser.find_element(
        By.CSS_SELECTOR, 'label .nowrap'
    ).text.strip()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text.strip()
    result = calculate_formula(formula, x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    alert = browser.switch_to.alert
    code = alert.text.rsplit(' ', 1)[1]
    print(code)
    alert.accept()
