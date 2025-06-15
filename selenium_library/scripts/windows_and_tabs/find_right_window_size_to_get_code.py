from selenium_library.browser_setup import browser

# for headed mode only

# fmt: off
window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
# fmt: on

with browser:
    browser.get('https://parsinger.ru/window_size/2/index.html')

    window_size = browser.get_window_size()
    width_border = window_size['width'] - browser.execute_script(
        'return window.innerWidth'
    )
    height_border = window_size['height'] - browser.execute_script(
        'return window.innerHeight'
    )

    found = False
    for x in window_size_x:
        if found:
            break
        for y in window_size_y:
            browser.set_window_size(x + width_border, y + height_border)
            result = browser.find_element('css selector', '#result').text
            if result.strip():
                right_size = {'width': x, 'height': y}
                print(right_size, result)
                found = True
                break
