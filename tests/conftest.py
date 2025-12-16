import pytest
from base.pages import browser_factory, MainPage
from base.config import BROWSER_NAME, TARGET_URL

@pytest.fixture(scope='session')
def driver(request):
    with browser_factory(BROWSER_NAME) as driver:
        yield driver


@pytest.fixture()
def main_page(driver):
    return MainPage(driver, TARGET_URL)
