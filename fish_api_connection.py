import requests

# Генерация производится за счёт api сайта РыбаТекст
# Документация: https://fish-text.ru/api
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
