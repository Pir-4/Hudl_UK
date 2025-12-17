from base.asserts import assert_equals, assert_item_loaded
from base.pages import LogInPage, UserMainAccPage
from base.logger import logger


def open_page(page, expected_page_title, is_close_privacy_window=False):
    logger.info("[Step] Opening page")
    page.open()
    assert_equals(
        page.title, expected_page_title, "Title mismatch"
    )
    if is_close_privacy_window:
        page.close_privacy_window()


def move_to_login_page(page) -> LogInPage:
    logger.info("[Step] Moving to login page")
    page.click_login()
    login_page = page.click_hudl_login()
    assert_item_loaded(
        login_page.is_email_input_displayed, "Login page"
    )
    return login_page


def set_username(page: LogInPage, username, is_move_next=False):
    logger.info(f"[Step] Setting username: {username}")
    page.set_email_input(username)
    if is_move_next:
        page.click_continue_button()
    return page


def set_password(page: LogInPage, password, is_move_next=False) -> UserMainAccPage | LogInPage:
    logger.info(f"Setting password: {password}")
    assert_item_loaded(
        page.is_password_input_displayed, "Password input"
    )
    page.set_password_input(password)
    if is_move_next:
        page.click_continue_button()
        return page.get_user_main_acc_page()
    return page
