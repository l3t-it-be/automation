from selenium.webdriver.common.by import By

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://suninjuly.github.io/selects1.html')

    num1 = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
    num2 = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
    result = num1 + num2

    browser.find_element(By.CSS_SELECTOR, 'select').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, 'button').click()

    alert = browser.switch_to.alert
    code = alert.text.rsplit(' ', 1)[1]
    print(code)
    alert.accept()
