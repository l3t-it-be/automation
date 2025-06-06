import requests

target_url = 'http://31.130.149.237/ua_trainer'


with requests.Session() as session:
    ua_response = session.get('http://31.130.149.237/ua_trainer/list').json()

    for user_agent in ua_response['user_agents']:
        session.headers.update({'User-Agent': user_agent})

        try:
            response = session.get(target_url)
            data = response.json()

            if data['password'] != '0':
                print(f'✅ Найден верный User-Agent: {user_agent}')
                print(f'🔑 Пароль: {data['password']}')
                break

        except Exception as e:
            print(f'⚠ Ошибка User-Agent {user_agent}: {e}')
