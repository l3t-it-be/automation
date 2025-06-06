import requests

headers = {
    'User-Agent': 'Chromezilla',
    'Accept': 'All what you give',
    'Accept-Language': 'English, Russian, German, Ukrainian',
    'Accept-Encoding': 'peace, love, understanding',
    'Referer': 'k-pax.com',
    'DFSHDRFAEHERHRAEH': 'where_did_you_come_from.com',
}

response = requests.get('http://31.130.149.237/user_agent', headers=headers)
