from dotenv import load_dotenv
from os import environ


load_dotenv()
POSTGRES_HOST = environ.get("POSTGRES_HOST")
POSTGRES_DB = environ.get("POSTGRES_DB")
POSTGRES_USER = environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD")
POSTGRES_PORT = environ.get("POSTGRES_PORT")
