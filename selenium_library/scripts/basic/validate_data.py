from selenium_library.browser_setup import browser

with browser:
    url = 'https://www.wikipedia.org/'
    browser.get(url)

    current_url = browser.current_url
    assert current_url == url, f'Expected URL: {url}, actual: {current_url}'

    expected_title = 'Wikipedia'
    current_title = browser.title
    assert (
        current_title == expected_title
    ), f'Expected title: {expected_title}, actual: {current_title}'

    print(browser.page_source)
