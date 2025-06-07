from selenium.webdriver import ActionChains

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.7/5/index.html')

    buttons = browser.find_elements('css selector', 'button')
    actions = ActionChains(browser)

    for button in buttons:
        browser.execute_script(
            'return arguments[0].scrollIntoView(true);', button
        )
        value = button.get_attribute('value')
        actions.click_and_hold(button).pause(float(value)).release(
            button
        ).perform()

    alert = browser.switch_to.alert
    result = alert.text
    print(result)
    alert.accept()
