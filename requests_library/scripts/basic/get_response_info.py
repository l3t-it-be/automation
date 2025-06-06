from requests_library.requests_setup import get_web_data

response = get_web_data(
    'https://parsinger.ru/selenium/6/6.3.1/index.html', return_response=True
)
print(
    response.status_code,
    response.text,
    response.headers,
    response.cookies,
    sep='\n',
)
