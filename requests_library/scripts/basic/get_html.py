from requests_library.requests_setup import get_web_data

html = get_web_data('https://parsinger.ru/3.4/2/index.html')
print(html)
