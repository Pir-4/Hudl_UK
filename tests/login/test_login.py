from base.config import TEST_EMAIL, TEST_PASSWORD
from base import steps
from base.asserts import  assert_item_loaded, assert_equals
from .constants import MAIN_PAGE_TITLE


def test_happy_login_path(main_page):
    steps.open_page(main_page, MAIN_PAGE_TITLE, True)
    login_page = steps.move_to_login_page(main_page)
    steps.set_username(login_page, TEST_EMAIL, True)
    user_main_acc_page = steps.set_password(login_page, TEST_PASSWORD, True)
    assert_item_loaded(
        user_main_acc_page.is_page_loaded, 'User Home Page'
    )


def test_email_input_validation(main_page, email_validator_param):
    input_email, is_valid = email_validator_param
    steps.open_page(main_page, MAIN_PAGE_TITLE, True)
    login_page = steps.move_to_login_page(main_page)
    steps.set_username(login_page, input_email, True)
    if is_valid:
        assert_item_loaded(
            login_page.is_password_input_displayed, "Password input"
        )
    else:
        error_message = login_page.get_error_message()
        assert_equals(
            'Enter a valid email.', error_message, 'Invalid email error message')

