from selenium_library.browser_setup import browser
from selenium_library.useful_functions import calculate_formula

with browser:
    browser.get('https://suninjuly.github.io/execute_script.html')

    formula = browser.find_element(
        'css selector', 'label .nowrap'
    ).text.strip()
    x = browser.find_element('css selector', '#input_value').text.strip()
    result = calculate_formula(formula, x)

    browser.find_element('css selector', '#answer').send_keys(result)
    browser.execute_script('window.scrollBy(0, 150);')

    browser.find_element('css selector', '#robotCheckbox').click()
    browser.find_element('css selector', '#robotsRule').click()
    browser.find_element('css selector', 'button').click()

    alert = browser.switch_to.alert
    code = alert.text.rsplit(' ', 1)[1]
    print(code)
    alert.accept()
