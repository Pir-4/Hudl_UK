from base.asserts import assert_equals
from .constants import (
    EMAIL_INVALID_ERROR_MESSAGE, EMAIL_REQUIRED_ERROR_MESSAGE,
    PASSWORD_INCORRECT_ERROR_MESSAGE, PASSWORD_EMPTY_ERROR_MESSAGE,
)


def assert_username_error(login_page, input_username):
    expected_error = EMAIL_INVALID_ERROR_MESSAGE
    if input_username:
        actual_error = login_page.get_invalid_email_error_message()
    else:
        expected_error = EMAIL_REQUIRED_ERROR_MESSAGE
        actual_error = login_page.get_required_username_error_message()

    assert_equals(
        actual_error, expected_error, 'Email/Username error message'
    )


def assert_password_error(login_page, input_username):
    expected_error = PASSWORD_INCORRECT_ERROR_MESSAGE
    actual_error = login_page.get_password_error_message()
    if not input_username:
        expected_error = PASSWORD_EMPTY_ERROR_MESSAGE

    assert_equals(
        actual_error, expected_error, 'Password error message'
    )
