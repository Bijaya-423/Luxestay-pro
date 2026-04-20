# Core configs & settings
 # Env variables, settings
import os
from dotenv import load_dotenv

# load_dotenv()
class Settings:
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')

    SECRET_KEY = os.getenv('SECRET_KEY')
    ALGORITHM = os.getenv('ALGORITHM')
    # ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30))
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30))

    
settings = Settings()


