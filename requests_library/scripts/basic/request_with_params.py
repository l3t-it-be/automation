from requests_library.requests_setup import get_web_data

my_params = {'q': 'python requests', 'page': 2}

response = get_web_data(
    'https://captcha-parsinger.ru/search',
    params=my_params,
    return_response=True,
    check_status=False,
)
print(response.url)
