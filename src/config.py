from os import environ

from dotenv import load_dotenv

load_dotenv()

# Database
DB_HOST = environ.get('POSTGRES_HOST', 'db')
DB_PORT = environ.get('POSTGRES_PORT', 5432)
DB_NAME = environ.get('POSTGRES_NAME', 'postgres')
DB_USER = environ.get('POSTGRES_USER', 'postgres')
DB_PASSWORD = environ.get('POSTGRES_PASSWORD', '123456')

# Test database
DB_HOST_TEST = environ.get("TEST_POSTGRES_HOST", 'db_test')
DB_PORT_TEST = environ.get("TEST_POSTGRES_PORT", 5432)
DB_NAME_TEST = environ.get("TEST_POSTGRES_NAME", 'postgres')
DB_USER_TEST = environ.get("TEST_POSTGRES_USER", 'postgres')
DB_PASSWORD_TEST = environ.get("TEST_POSTGRES_PASSWORD", '123456')
