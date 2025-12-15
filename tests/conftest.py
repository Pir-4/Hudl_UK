import pytest
from base.pages import get_browser
from base.config import BROWSER_NAME

@pytest.fixture(scope='session')
def driver(request):
    with get_browser(BROWSER_NAME) as driver:
        yield driver
