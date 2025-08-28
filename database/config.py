import os
from dotenv import load_dotenv


load_dotenv()

POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB=os.getenv('POSTGRES_DB')

APP_DB_USER=os.getenv('APP_DB_USER')
APP_DB_PASSWORD=os.getenv('APP_DB_PASSWORD')

if not POSTGRES_DB or not POSTGRES_USER or not POSTGRES_PASSWORD:
    raise Exception(f"There is not enogh data in .env")

if not APP_DB_USER or not APP_DB_PASSWORD:
    APP_DB_USER = POSTGRES_USER
    APP_DB_PASSWORD = POSTGRES_PASSWORD


class Config:
    DATABASE_URL =f"postgresql+psycopg2://{APP_DB_USER}:{APP_DB_PASSWORD}@db:5432/{POSTGRES_DB}" 
    DATABASE_URL_ALEMBIC =f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}" 

