from base.asserts import assert_equals, assert_item_loaded
from base.pages import MainPage, LogInPage, UserHomePage
from base.logger import logger


def open_page(
        page: MainPage,
        expected_page_title: str,
        is_close_privacy_window: bool = True
):
    logger.info("[Step] Opening page")
    page.open()
    assert_equals(
        page.title, expected_page_title, "Title mismatch"
    )
    if is_close_privacy_window:
        page.close_privacy_window()


def move_to_login_page(page: MainPage) -> LogInPage:
    logger.info("[Step] Moving to login page")
    page.click_login()
    login_page = page.click_hudl_login()
    assert_item_loaded(
        login_page.is_email_input_displayed, "Login page"
    )
    return login_page


def set_username(
        page: LogInPage,
        username: str,
        is_click_button: bool = True
) -> LogInPage:
    logger.info(f"[Step] Setting username: {username}")
    page.set_email_input(username)
    if is_click_button:
        page.click_continue_button()
    return page


def set_password(
        page: LogInPage, password: str, is_click_button: bool = True,
        is_move_next: bool = True
) -> UserHomePage | LogInPage:
    logger.info(f"Setting password: {password}")
    assert_item_loaded(
        page.is_password_input_displayed, "Password input"
    )
    page.set_password_input(password)
    if is_click_button:
        page.click_continue_button()
    return page.get_user_home_page() if is_move_next else page
