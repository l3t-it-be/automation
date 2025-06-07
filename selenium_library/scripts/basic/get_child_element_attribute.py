from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.1/index.html')
    child_element = browser.find_element(
        'css selector', '#parent_id .child_class'
    )
    child_element.click()
    print(child_element.get_attribute('password'))
