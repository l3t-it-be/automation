from selenium.webdriver import ActionChains

from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless mode
    browser.get('https://parsinger.ru/selenium/5.10/4/index.html')

    balls = browser.find_elements('css selector', '.ball_color')

    for ball in balls:
        color = (
            ball.get_attribute('class').split('_ball')[0].split()[1].strip()
        )
        basket = browser.find_element('css selector', f'.basket_color.{color}')
        actions = ActionChains(browser)
        actions.drag_and_drop(ball, basket).perform()

    secret_message = browser.find_element('css selector', '.message').text
    print(secret_message)
