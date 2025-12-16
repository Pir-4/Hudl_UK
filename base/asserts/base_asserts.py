from base.logger import logger

def assert_equals(actual, expected, error_message=None):
    logger.debug(f'Asserting {actual} ==> {expected}')
    assert actual == expected, error_message