from base.asserts import assert_equals

def open_page(page, expected_page_title):
    page.open()
    assert_equals(page.title, expected_page_title, "Title mismatch")