from base.asserts import assert_equals
from base.pages import LogInPage, UserMainAccPage


def open_page(page, expected_page_title, is_close_privacy_window=False):
    page.open()
    assert_equals(
        page.title, expected_page_title, "Title mismatch"
    )
    if is_close_privacy_window:
        page.close_privacy_window()


def move_to_login_page(page) -> LogInPage:
    page.click_login()
    return page.click_hudl_login()


def set_username(page: LogInPage, username, is_move_next=False):
    page.set_email_input(username)
    if is_move_next:
        page.click_login2()


def set_password(page: LogInPage, password, is_move_next=False) -> UserMainAccPage | None:
    page.set_password_input(password)
    if is_move_next:
        page.click_login2()
        return page.get_user_main_acc_page()
    return None
