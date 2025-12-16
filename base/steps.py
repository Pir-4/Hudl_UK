from base.asserts import assert_equals


def open_page(page, expected_page_title, is_close_privacy_window=False):
    page.open()
    assert_equals(
        page.title, expected_page_title, "Title mismatch"
    )
    if is_close_privacy_window:
        page.close_privacy_window()


def move_to_login_page(page):
    page.click_login()
    page.click_hudl_login()


def set_username(page, username, is_move_next=False):
    page.set_email_input(username)
    if is_move_next:
        page.click_login2()


def set_password(page, password, is_move_next=False):
    page.set_password_input(password)
    if is_move_next:
        page.click_login2()
