import requests
from fake_useragent import UserAgent

os_list = ['Mac OS X', 'Windows', 'Android', 'Linux', 'iOS']
user_agents = [UserAgent(os=os_name) for os_name in os_list]
headers = [{'User-Agent': user_agent.random} for user_agent in user_agents]

password = []
with requests.Session() as session:
    for header in headers:
        session.headers.update(header)
        part_of_pass = int(
            session.get('http://31.130.149.237/os-challenge/os').json()[
                'part_of_password'
            ]
        )
        password.append(part_of_pass)

print(sum(password))
