from base.config import TEST_EMAIL, TEST_PASSWORD
from base.logger import  logger


def test_login(driver):
    driver.get("http://hudl.com/")
    assert False
