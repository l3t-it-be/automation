import requests

from requests_library.requests_setup import get_web_data

# fmt: off
amounts_per_give_currency = {
        'USD': 150, 'EUR': 120, 'RUB': 20000, 'BYN': 50, 'JPY': 50000,
        'GBP': 250, 'CAD': 1000, 'BTC': 0.01, 'ETH': 0.5, 'SOL': 10,
        'USDT': 150, 'ADA': 300, 'DOGE': 5000, 'XRP': 1000, 'BNB': 1,
        'USDC': 150, 'TRX': 10000
}
# fmt: on
currencies = tuple(amounts_per_give_currency)

results = []

with requests.Session() as session:
    for give_currency in currencies:
        for get_currency in currencies:
            if give_currency == get_currency:
                continue

            # fmt: off
            data = {
                'GiveName': give_currency,
                'GetName': get_currency,
                'Sum': amounts_per_give_currency[give_currency],
                'Direction': 0
            }
            # fmt: on

            url = 'http://31.130.149.237/api/v1/ajax/GetSum'
            response = get_web_data(
                url, session=session, params=data, json=True
            )
            result = round(response['getSum'], 2)
            results.append(result)

print(sum(results))
