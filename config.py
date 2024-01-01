# config.py
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    # General Flask configuration
    DEBUG = os.getenv('DEBUG', True)
    SECRET_KEY = os.getenv('SECRET_KEY')
    PORT = int(os.getenv('PORT', 4500))

    # Database configuration
    user = os.getenv('DB_USER')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    database = os.getenv('DATABASE')

    # Construct the encoded URI
    encoded_password = quote_plus(password)

    SQLALCHEMY_DATABASE_URI = f'mysql://{user}:{encoded_password}@{host}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # CORS configuration
    CORS_HEADERS = 'Content-Type'
