from selenium_library.browser_setup import browser

with browser:
    browser.get('https://hyperskill.org/courses')

    header_links = browser.find_elements('css selector', '.nav-link')
    print(len(header_links))

    print('For Business:', header_links[3].text)
