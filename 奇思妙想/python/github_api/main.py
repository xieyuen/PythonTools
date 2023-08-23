import requests

from exceptions import ClientError, ServerError

def get_repos(query, *, sort='stars'):
    url = f'https://api.github.com/search/repositories?q={query}&sort={sort}'
    r = requests.get(url)
    if r.status_code != 200:
        if 400 <= r.status_code < 500:
            raise ClientError()
        elif 500 <= r.status_code < 600:
            raise ServerError()

    # connected to the server
    data = r.json()



def print_data(datas: dict):
    for data_key in datas.keys:
        print(datas[data_key])
        if isinstance(datas[data_key], dict):
            print_data(datas[data_key])
