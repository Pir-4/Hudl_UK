from base.logger import logger

def assert_item_loaded(check_fuc, page_name):
    logger.debug(f'Asserting {page_name} item loaded')
    assert check_fuc(), f"{page_name} is not loaded"
