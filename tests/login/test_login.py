from base.config import TEST_EMAIL, TEST_PASSWORD
from base import steps
from .constants import MAIN_PAGE_TITLE


def test_login(main_page):
    steps.open_page(main_page, MAIN_PAGE_TITLE, True)
    steps.move_to_login_page(main_page)
    steps.set_username(main_page, TEST_EMAIL, True)
    steps.set_password(main_page, TEST_PASSWORD, True)
    main_page.wait_home_page()
