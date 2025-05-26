from selenium.webdriver.common.by import By

from selenium_library.browser_setup import browser
from selenium_library.useful_functions import calculate_formula

with browser:
    browser.get('https://suninjuly.github.io/execute_script.html')

    formula = browser.find_element(
        By.CSS_SELECTOR, 'label .nowrap'
    ).text.strip()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text.strip()
    result = calculate_formula(formula, x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    browser.execute_script('window.scrollBy(0, 150);')

    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, 'button').click()

    alert = browser.switch_to.alert
    code = alert.text.rsplit(' ', 1)[1]
    print(code)
    alert.accept()
