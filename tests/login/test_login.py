from base.config import TEST_EMAIL, TEST_PASSWORD
from base import steps
from .constants import MAIN_PAGE_TITLE


def test_login(main_page):
    steps.open_page(main_page, MAIN_PAGE_TITLE, True)
    login_page = steps.move_to_login_page(main_page)
    steps.set_username(login_page, TEST_EMAIL, True)
    user_main_acc_page = steps.set_password(login_page, TEST_PASSWORD, True)
    user_main_acc_page.wait_home_page()
