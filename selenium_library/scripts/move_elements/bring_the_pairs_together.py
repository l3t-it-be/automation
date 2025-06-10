from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless mode
    browser.get('https://parsinger.ru/selenium/5.10/3/index.html')

    WebDriverWait(browser, 10).until(
        ec.visibility_of_all_elements_located(
            ('css selector', '#main_container div')
        )
    )

    squares = browser.find_elements('css selector', '.draganddrop')
    frames = browser.find_elements('css selector', '.draganddrop_end')

    actions = ActionChains(browser)
    for square, frame in zip(squares, frames):
        actions.click_and_hold(square).move_to_element(
            frame
        ).release().perform()

    browser.execute_script('window.scrollTo(0, 0);')

    result = browser.find_element('css selector', '#message').text
    print(result)
