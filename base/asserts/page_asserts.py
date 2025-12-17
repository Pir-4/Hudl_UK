from base.logger import logger

def assert_item_loaded(check_func, item_name):
    logger.debug(f'Asserting {item_name} item loaded')
    assert check_func(), f"{item_name} is not loaded"
