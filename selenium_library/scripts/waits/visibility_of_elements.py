from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

# fmt: off
ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB',
               'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I','jolHZqD1', 'ZM6Ms3tw',
               '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']
# fmt: on

with browser:
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')

    for id_to_find in ids_to_find:
        element = WebDriverWait(browser, 50, 0.01).until(
            ec.visibility_of_element_located(('id', id_to_find))
        )
        element.click()

    alert = browser.switch_to.alert
    result = alert.text
    print(result)
    alert.accept()
