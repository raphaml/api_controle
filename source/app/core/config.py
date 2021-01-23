import json

from typing import List
from typing import Optional

from pydantic import BaseSettings
from pydantic import Field
from pydantic import PostgresDsn
from pydantic import AnyUrl


def list_parse_fallback(v):
    try:
        return json.loads(v)
    except Exception as e:
        return v.split(',')


class Settings(BaseSettings):
    PROJECT_NAME: str = 'easy bar'
    API_URL: str = '/api'

    API_HOST: str = '0.0.0.0'
    API_PORT: int = 8000

    DEBUG: bool = False
    RELOAD: bool = False

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    class Config:
        json_loads = list_parse_fallback


settings = Settings()