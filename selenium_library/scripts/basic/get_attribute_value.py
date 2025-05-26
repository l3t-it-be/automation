from selenium.webdriver.common.by import By

from selenium_library.browser_setup import browser
from selenium_library.useful_functions import calculate_formula

with browser:
    browser.get('https://suninjuly.github.io/get_attribute.html')

    formula = browser.find_element(By.CSS_SELECTOR, 'h2 .nowrap').text.strip()
    x = (
        browser.find_element(By.CSS_SELECTOR, '#treasure')
        .get_attribute('valuex')
        .strip()
    )
    result = calculate_formula(formula, x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    alert = browser.switch_to.alert
    code = alert.text.rsplit(' ', 1)[1]
    print(code)
    alert.accept()
