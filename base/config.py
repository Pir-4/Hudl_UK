from dotenv import load_dotenv
from environs import env

load_dotenv()

TEST_EMAIL = env('TEST_EMAIL')
TEST_PASSWORD = env('TEST_PASSWORD')
LOGGER_LEVEL = env('LOGGER_LEVEL', 'INFO')