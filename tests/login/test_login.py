from base.config import TEST_EMAIL, TEST_PASSWORD
from base import steps
from base.asserts import assert_item_loaded, assert_equals
from .asserts import (
    assert_user_home_page, assert_username_error, assert_password_error,
)
from .constants import MAIN_PAGE_TITLE, LOGIN_PAGE_TITLE


def test_login_happy_path(main_page):
    steps.open_page(main_page, MAIN_PAGE_TITLE)
    # login
    login_page = steps.move_to_login_page(main_page)
    steps.set_username(login_page, TEST_EMAIL)
    # password
    user_home_page = steps.set_password(login_page, TEST_PASSWORD)
    # user home page
    assert_user_home_page(user_home_page)


def test_email_input_validation(main_page, email_validator_param):
    # data preparation
    input_email, is_display_password = email_validator_param
    # actions
    steps.open_page(main_page, MAIN_PAGE_TITLE)
    login_page = steps.move_to_login_page(main_page)
    steps.set_username(login_page, input_email)
    # asserts
    assert_equals(login_page.title, LOGIN_PAGE_TITLE, 'Login page title')
    if is_display_password:
        assert_item_loaded(
            login_page.is_password_input_displayed, "Password input"
        )
    else:
        assert_username_error(login_page, input_email)


def test_password_input_validation(main_page, password_validator_param):
    # data preparation
    input_email, input_password, is_right = password_validator_param
    # actions
    steps.open_page(main_page, MAIN_PAGE_TITLE, True)
    login_page = steps.move_to_login_page(main_page)
    steps.set_username(login_page, input_email, True)
    actual_page = steps.set_password(
        login_page, input_password, True, is_right
    )
    # asserts
    if is_right:
        assert_user_home_page(actual_page)
        return

    assert_equals(actual_page.title, LOGIN_PAGE_TITLE, 'Login page title')
    assert_password_error(login_page, input_password)


def test_edit_username(main_page):
    steps.open_page(main_page, MAIN_PAGE_TITLE, True)
    # actions
    login_page = steps.move_to_login_page(main_page)
    steps.set_username(login_page, TEST_EMAIL, True)
    assert_item_loaded(
        login_page.is_password_input_displayed, "Password input"
    )
    login_page.click_edit_link()
    # asserts
    assert_item_loaded(
        lambda: not login_page.is_password_input_displayed(),
        "Password input"
    )
    assert_equals(login_page.get_email_value(), TEST_EMAIL, 'Email address')
