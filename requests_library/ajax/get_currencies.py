from requests_library.requests_setup import get_web_data

# fmt: off
data = {
    'GiveName': 'JPY',
    'GetName': 'DOGE',
    'Sum': 51284.43,
    'Direction': 0
}
# fmt: on

response = get_web_data(
    'http://31.130.149.237/api/v1/ajax/GetSum', params=data, json=True
)
print(round(response['getSum'], 2))
