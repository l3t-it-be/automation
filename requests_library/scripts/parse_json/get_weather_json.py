from requests_library.requests_setup import get_web_data

min_temp = float('inf')
date = None

weather_data = get_web_data(
    'https://parsinger.ru/3.4/1/json_weather.json', json=True
)
for entry in weather_data:
    temp = int(entry['Температура воздуха'].replace('°C', ''))
    if temp < min_temp:
        min_temp = temp
        date = entry['Дата']

print(min_temp, date)
