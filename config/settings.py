import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '..', '.env'))

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "passwd": os.getenv("DB_PASS", ""),
    "database": os.getenv("DB_NAME", "master_python"),
    "port": int(os.getenv("DB_PORT", 3306)),
}