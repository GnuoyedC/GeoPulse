from pathlib import Path
from dotenv import dotenv_values

# Define base directory and paths to .env files
BASE_DIR = Path(__file__).resolve().parent.parent
ENVAPI_PATH = BASE_DIR / '.env.gdeltapi'
ENVDB_PATH = BASE_DIR / '.env.db'
ENVDEV_PATH = BASE_DIR / '.env.dev'
ENVDJANGO_PATH = BASE_DIR / '.env.django'

class Config:
    API_CONF = dotenv_values(ENVAPI_PATH)
    DB_CONF = dotenv_values(ENVDB_PATH)
    DEV_CONF = dotenv_values(ENVDEV_PATH)
    DJANGO_CONF = dotenv_values(ENVDJANGO_PATH)

    @classmethod
    def API(cls):
        return cls.API_CONF

    @classmethod
    def DB(cls):
        return cls.DB_CONF

    @classmethod
    def DEV(cls):
        return cls.DEV_CONF

    @classmethod
    def DJANGO(cls):
        return cls.DJANGO_CONF
