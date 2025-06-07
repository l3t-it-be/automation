from selenium_library.browser_setup import browser, random_generator

with browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')

    forms = browser.find_elements('css selector', 'input.form')
    values = (
        random_generator.first_name(),
        random_generator.last_name(),
        random_generator.first_name(),
        random_generator.random_int(10, 90),
        random_generator.city(),
        random_generator.email(),
    )
    for form, value in zip(forms, values):
        form.send_keys(value)

    browser.find_element('css selector', 'input#btn').click()
    result = browser.find_element('css selector', '#result').text
    print(result)
