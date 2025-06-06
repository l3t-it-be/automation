import requests
from fake_useragent import UserAgent

# fmt: off
combinations = {
    'valid_combinations': [
        {'browser': 'Chrome', 'os': 'Windows'},
        {'browser': 'Chrome', 'os': 'Mac OS X'},
        {'browser': 'Chrome', 'os': 'Linux'},
        {'browser': 'Safari', 'os': 'Mac OS X'},
        {'browser': 'Firefox', 'os': 'Windows'},
        {'browser': 'Firefox', 'os': 'Linux'},
        {'browser': 'Firefox', 'os': 'Mac OS X'},
        {'browser': 'Edge', 'os': 'Windows'},
    ]
}
# fmt: on

password = []

with requests.Session() as session:
    for combo in combinations['valid_combinations']:
        ua = UserAgent(browsers=[combo['browser']], os=combo['os'])
        session.headers.update({'User-Agent': ua.random})

        response = session.get(
            'http://31.130.149.237/browser-compatibility/browser-os-check'
        ).json()

        part_of_pass = int(response['part_of_password'])
        password.append(part_of_pass)

print(sum(password))
