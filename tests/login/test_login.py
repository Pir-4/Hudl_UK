from base.config import TEST_EMAIL, TEST_PASSWORD

def test_login(main_page):
    main_page.open()
    main_page.close_cookie()
    main_page.click_login()
    main_page.click_hudl_login()
    main_page.set_email_input(TEST_EMAIL)
    main_page.click_login2()
    main_page.set_password_input(TEST_PASSWORD)
    main_page.click_login2()
    main_page.wait_home_page()
