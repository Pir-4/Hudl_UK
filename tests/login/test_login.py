from base.config import TEST_EMAIL, TEST_PASSWORD
from base import steps
from base.asserts import assert_item_loaded, assert_equals
from .asserts import assert_username_error
from .constants import (
    MAIN_PAGE_TITLE, EMAIL_INVALID_ERROR_MESSAGE, EMAIL_REQUIRED_ERROR_MESSAGE,
)


def test_happy_login_path(main_page):
    steps.open_page(main_page, MAIN_PAGE_TITLE, True)
    # login
    login_page = steps.move_to_login_page(main_page)
    steps.set_username(login_page, TEST_EMAIL, True)
    # password
    user_home_page = steps.set_password(
        login_page, TEST_PASSWORD, True
    )
    # user home page
    assert_item_loaded(
        user_home_page.is_page_loaded, 'User Home Page'
    )


def test_email_input_validation(main_page, email_validator_param):
    input_email, is_display_password = email_validator_param
    steps.open_page(main_page, MAIN_PAGE_TITLE, True)
    login_page = steps.move_to_login_page(main_page)
    steps.set_username(login_page, input_email, True)
    if is_display_password:
        assert_item_loaded(
            login_page.is_password_input_displayed, "Password input"
        )
    else:
        assert_username_error(login_page, input_email)
