def assert_item_loaded(check_fuc, page_name):
    assert check_fuc(), f"{page_name} is not loaded"
