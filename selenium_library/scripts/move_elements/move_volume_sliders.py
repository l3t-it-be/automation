from selenium.webdriver import Keys

from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless mode
    browser.get('https://parsinger.ru/selenium/5.10/6/index.html')

    sliders = browser.find_elements('css selector', '.volume-slider')
    target_values = browser.find_elements('css selector', '.target-value')

    for slider, target_value in zip(sliders, target_values):
        current_value = int(slider.get_attribute('value'))
        target_value = int(target_value.text)

        while current_value != target_value:
            if current_value < target_value:
                slider.send_keys(Keys.ARROW_RIGHT)
                current_value += 1
            elif current_value > target_value:
                slider.send_keys(Keys.ARROW_LEFT)
                current_value -= 1

    result = browser.find_element('css selector', '#message').text
    print(result)
