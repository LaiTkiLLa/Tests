import requests

def get_info(ya_token, folder_name):
    url_ya = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {"Authorization": ya_token}
    path = {"path" : folder_name}
    response = requests.get(url=url_ya, headers=headers, params=path)
    if response.status_code == 401:
        return 'код 401, некорректный яндекс токен'
    if response.status_code == 503:
        return 'Сервис временно недоступен, попробуйте позже'
    if response.status_code == 404:
        return 'Папки не существует'
    if response.status_code == 200:
        return response.status_code

def new_folder(ya_token, folder_name):
    url_ya = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {"Authorization": ya_token}
    path = {"path": folder_name}
    response = requests.put(url=url_ya, headers=headers, params=path)
    if response.status_code == 409:
        return f'Ресурс {folder_name} уже существует'
    if response.status_code == 201:
        return response.status_code

def delete_folder(ya_token, folder_name):
    url_ya = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {"Authorization": ya_token}
    path = {"path": folder_name}
    response = requests.delete(url=url_ya, headers=headers, params=path)
    if response.status_code == 204:
        return response.status_code
    if response.status_code == 404:
        return 'Такого ресурса не сущесвует'
    else:
        return 'Что то пошло не так'

