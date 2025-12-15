from dotenv import load_dotenv
from environs import env

load_dotenv()

TEST_EMAIL = env.str('TEST_EMAIL')
TEST_PASSWORD = env.str('TEST_PASSWORD')
LOGGER_LEVEL = env.log_level('LOGGER_LEVEL', 'INFO')
BROWSER_NAME = env.str('BROWSER_NAME', 'chrome')
TARGET_URL = env.str('TARGET_URL', 'http://hudl.com/')
