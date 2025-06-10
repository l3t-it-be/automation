from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/draganddrop/3/index.html')

    blue_square = browser.find_element('css selector', '#block1')
    points = browser.find_elements('css selector', '.controlPoint')

    actions = ActionChains(browser)

    actions.click_and_hold(blue_square)
    for point in points:
        actions.move_to_element(point)
    actions.move_to_element(points[0]).perform()

    token = WebDriverWait(browser, 5).until(
        ec.visibility_of_element_located(('css selector', '#message'))
    )
    print(token.text)
