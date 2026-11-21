import psycopg
import os
from dotenv import load_dotenv

load_dotenv()
DB_CONFIG = {
    "dbname": os.getenv("DB_name"),
    "user": os.getenv("DB_user"),
    "password": os.getenv("DB_pass"),
    "host": os.getenv("DB_host"),
    "port": os.getenv("DB_port")
}

def get_connection():
    return psycopg.connect(**DB_CONFIG)

