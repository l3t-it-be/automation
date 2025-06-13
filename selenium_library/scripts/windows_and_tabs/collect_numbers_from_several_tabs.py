from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/8/8.1.2/index.html')

    links = browser.find_elements('css selector', 'a[href]')
    for link in links:
        browser.execute_script(
            'window.open(arguments[0], "_blank");', link.get_attribute('href')
        )

    all_numbers = []
    tabs = browser.window_handles

    wait = WebDriverWait(browser, 5, poll_frequency=1)

    for tab in tabs[1:]:
        browser.switch_to.window(tab)
        wait.until(
            ec.presence_of_element_located(
                ('css selector', '.numbers-container')
            )
        )
        numbers = [
            int(num.text)
            for num in browser.find_elements('css selector', '.number')
            if num.text.isdigit()
        ]
        all_numbers.extend(numbers)

    browser.switch_to.window(tabs[0])

    browser.find_element('css selector', 'input').send_keys(sum(all_numbers))
    wait.until(
        ec.text_to_be_present_in_element(('css selector', '#timer'), '0')
    )
    browser.find_element('css selector', 'button#checkButton').click()

    password = browser.find_element('css selector', '#passwordDisplay')
    print(password.text.split(':')[1].strip())
