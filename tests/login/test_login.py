def test_login(main_page):
    main_page.open()
    main_page.close_cookie()
    main_page.click_login()
    main_page.click_hudl_login()
    assert False
