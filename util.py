import json, os


def get_server_info_value(key: str):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_ROOT = os.path.join(BASE_DIR, 'server_info.json') 

    with open(FILE_ROOT, mode='rt', encoding='utf-8') as file:
        data = json.load(file)
        for k, v in data.items():
            if k == key:
                return v
        raise ValueError('서버정보를 확인할 수 없습니다.')