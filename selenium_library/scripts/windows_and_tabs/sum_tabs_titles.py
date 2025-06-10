from selenium_library.browser_setup import browser

url_nums = (1, 2)
chars_to_exclude = (('4', '3', '9'), ('7', '8', '0'))

nums = []
with browser:
    for url_num, chars in zip(url_nums, chars_to_exclude):
        url = f'https://parsinger.ru/selenium/8/8.1/site{url_num}/'
        browser.get(url)
        num = int(
            ''.join([char for char in browser.title if char not in chars])
        )
        nums.append(num)

print(sum(nums))
