from base.asserts import assert_equals, assert_item_loaded
from base.pages import MainPage, LogInPage, UserHomePage
from .constants import (
    EMAIL_INVALID_ERROR_MESSAGE, EMAIL_REQUIRED_ERROR_MESSAGE,
    PASSWORD_INCORRECT_ERROR_MESSAGE, PASSWORD_EMPTY_ERROR_MESSAGE,
    USER_HOMEPAGE_TITLE,
)


def assert_user_home_page(page: UserHomePage):
    assert_item_loaded(
        page.is_page_loaded, 'User home page'
    )
    assert_equals(page.title, USER_HOMEPAGE_TITLE, 'User page title')


def assert_username_error(login_page: LogInPage, input_username: str):
    expected_error = EMAIL_INVALID_ERROR_MESSAGE
    if input_username:
        actual_error = login_page.get_invalid_email_error_message()
    else:
        expected_error = EMAIL_REQUIRED_ERROR_MESSAGE
        actual_error = login_page.get_required_username_error_message()

    assert_equals(
        actual_error, expected_error, 'Email/Username error message'
    )


def assert_password_error(login_page: LogInPage, input_username: str):
    expected_error = PASSWORD_INCORRECT_ERROR_MESSAGE
    if input_username:
        actual_error = login_page.get_incorrect_password_error_message()
    else:
        expected_error = PASSWORD_EMPTY_ERROR_MESSAGE
        actual_error = login_page.get_required_password_error_message()

    assert_equals(
        actual_error, expected_error, 'Password error message'
    )
