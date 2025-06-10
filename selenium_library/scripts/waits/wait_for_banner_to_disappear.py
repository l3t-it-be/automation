from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless mode
    browser.get('https://parsinger.ru/selenium/5.9/4/index.html')

    close_ad_button = browser.find_element('css selector', '#closeBtn')
    close_ad_button.click()

    WebDriverWait(browser, 10).until(
        ec.invisibility_of_element_located(('css selector', '#ad'))
    )

    click_me_button = browser.find_element('css selector', 'button')
    WebDriverWait(browser, 5).until(
        ec.element_to_be_clickable(click_me_button)
    ).click()

    message = browser.find_element('css selector', '#message').text
    print(message)
