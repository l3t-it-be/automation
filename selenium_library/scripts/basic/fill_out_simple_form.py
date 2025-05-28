from selenium_library.browser_setup import browser, random_generator

with browser:
    browser.get('https://suninjuly.github.io/simple_form_find_task.html')

    browser.find_element('css selector', 'input[name="first_name"]').send_keys(
        random_generator.first_name()
    )
    browser.find_element('css selector', 'input[name="last_name"]').send_keys(
        random_generator.last_name()
    )
    browser.find_element('css selector', '.city').send_keys(
        random_generator.city()
    )
    browser.find_element('css selector', '#country').send_keys(
        random_generator.country()
    )
    browser.find_element('css selector', '#submit_button').click()

    alert = browser.switch_to.alert
    code = alert.text.rsplit(' ', 1)[1]
    print(code)
    alert.accept()
