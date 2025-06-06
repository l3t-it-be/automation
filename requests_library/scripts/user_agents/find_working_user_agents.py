import logging

import requests
from fake_useragent import UserAgent

logging.getLogger('fake_useragent').setLevel(logging.CRITICAL)

browser_os_combinations = [
    {'browser': ['Chrome'], 'os': 'Windows'},
    {'browser': ['Chrome'], 'os': 'Mac OS X'},
    {'browser': ['Chrome'], 'os': 'Linux'},
    {'browser': ['Chrome'], 'os': 'Android'},
    {'browser': ['Firefox'], 'os': 'Windows'},
    {'browser': ['Firefox'], 'os': 'Mac OS X'},
    {'browser': ['Firefox'], 'os': 'Linux'},
    {'browser': ['Firefox'], 'os': 'Android'},
    {'browser': ['Safari'], 'os': 'Mac OS X'},
    {'browser': ['Edge'], 'os': 'Windows'},
    {'browser': ['Opera'], 'os': 'Windows'},
    {'browser': ['Opera'], 'os': 'Mac OS X'},
    {'browser': ['Opera'], 'os': 'Linux'},
    {'browser': ['Opera'], 'os': 'Android'},
    {'browser': ['Mobile Safari'], 'os': 'iOS'},
    {'browser': ['Opera'], 'os': 'iOS'},
    {'browser': ['Chrome'], 'os': 'iOS'},
]

password = []
user_agents = []

with requests.Session() as session:
    for combo in browser_os_combinations:
        ua = UserAgent(browsers=combo['browser'], os=combo['os'])
        session.headers.update({'User-Agent': ua.random})

        response = session.get('http://31.130.149.237/right_combination/check')
        if response.ok:
            data = response.json()
            user_agent = {
                'browser': data['browser'],
                'os': data['os'],
            }
            user_agents.append(user_agent)
            part_of_pass = int(data['part_of_password'])
            password.append(part_of_pass)

print(f'Valid User-Agents: {user_agents},\nSum passwords: {sum(password)}')
