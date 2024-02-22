import os
from typing import Dict
from dotenv import load_dotenv, dotenv_values
from src.common.singleton import SingletonMeta


class Config(metaclass=SingletonMeta):
    _configs: Dict = {}

    def __init__(self):
        env = os.environ.get('ENV')
        if env == 'prod':
            load_dotenv('.env')
        else:
            env = 'dev'
            load_dotenv('.env.dev')

        self._configs = dict.fromkeys(dotenv_values())
        for key, _ in self._configs.items():
            self._configs[key] = os.environ.get(key)

        self._configs['ENV'] = env

    def get(self, key: str, default: str = '') -> str:
        if key not in self._configs:
            return default

        return self._configs[key]

    def get_postgres_url(self) -> str:
        url = f"postgresql://{self._configs['POSTGRES_USERNAME']}:{self._configs['POSTGRES_PASSWORD']}@{self._configs['POSTGRES_HOST']}:{self._configs['POSTGRES_PORT']}/{self._configs['POSTGRES_DB_NAME']}"
        return url

