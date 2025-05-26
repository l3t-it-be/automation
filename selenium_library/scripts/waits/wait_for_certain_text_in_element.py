from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium_library.browser_setup import browser
from selenium_library.useful_functions import calculate_formula

with browser:
    browser.get('https://suninjuly.github.io/explicit_wait2.html')

    WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '100')
    )
    browser.find_element(By.CSS_SELECTOR, '#book').click()

    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    browser.execute_script(
        'return arguments[0].scrollIntoView(true)', input_field
    )

    formula = browser.find_element(
        By.CSS_SELECTOR, 'label .nowrap'
    ).text.strip()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text.strip()
    result = calculate_formula(formula, x)

    input_field.send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '#solve').click()

    alert = browser.switch_to.alert
    code = alert.text.rsplit(' ', 1)[1]
    print(code)
    alert.accept()
