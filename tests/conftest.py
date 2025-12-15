import pytest
from base.pages import get_browser, MainPage
from base.config import BROWSER_NAME, TARGET_URL

@pytest.fixture(scope='session')
def driver(request):
    with get_browser(BROWSER_NAME) as driver:
        yield driver


@pytest.fixture()
def main_page(driver):
    return MainPage(driver, TARGET_URL)
