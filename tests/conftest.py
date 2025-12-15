import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver(request):
    driver = webdriver.Chrome()
    yield driver
    driver.close()
