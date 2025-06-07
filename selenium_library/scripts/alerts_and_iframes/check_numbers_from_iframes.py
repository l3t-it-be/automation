from selenium.common import NoAlertPresentException

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.8/5/index.html')

    iframes = browser.find_elements('css selector', '#main_container iframe')
    for iframe in iframes:
        browser.switch_to.frame(iframe)
        browser.find_element('css selector', 'button').click()
        frame_num = browser.find_element('css selector', '#numberDisplay').text
        browser.switch_to.default_content()

        input_field = browser.find_element('css selector', 'input#guessInput')
        input_field.clear()
        input_field.send_keys(frame_num)

        check_button = browser.find_element('css selector', 'button#checkBtn')
        check_button.click()

        try:
            alert = browser.switch_to.alert
            result = alert.text
            print(result)
            alert.accept()
            break
        except NoAlertPresentException:
            pass
