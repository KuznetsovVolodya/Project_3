import requests

address = 'https://fish-text.ru/get'
api_server = address


def gen_prof():
    params = {
        'type': 'title',
        'number': 1,
        'format': 'json',
    }
    response = requests.get(api_server, params=params).json()
    b = response['text']
    return b
