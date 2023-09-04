import requests

def create_folder(path, token):
    """Создание папки на ЯД"""
    headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
        }
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    response = requests.put(f'{url}?path={path}', headers=headers)
    sc = response.status_code
    return sc


