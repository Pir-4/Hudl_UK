import pytest
from base.config import TEST_EMAIL, TEST_PASSWORD


@pytest.fixture(params=[
    pytest.param(('test@test.com', True), id='valid'),
    pytest.param(('Test@Test.com', True), id='capitalize'),
    pytest.param(('test-4@test.com', True), id='number_and_punctuation'),
    pytest.param(('my.te4st-t@lk.c.com.net', True), id='complex'),
    pytest.param(
        ('xn--_@-wlcbbeejdu5d6bnh3g.xn--p1ai', False), id='punnycode'
    ),
    pytest.param(('мой_ящик@лучший.рф', True), id='local_lang'),
    pytest.param(('user.user2@gatech.global', True), id='with_sub_domain'),
    pytest.param(('twst@gta.globalgatechglobal', True), id='long_domain'),
    pytest.param(('test.test.com', False), id='web_address'),
    pytest.param(('test@testco.m', False), id='wrong_size_domain'),
    pytest.param(('test@test', False), id='not_complete_domain'),
    pytest.param(('test', False), id='string'),
    pytest.param(('', False), id='empty'),
])
def email_validator_param(request):
    return request.param


@pytest.fixture(params=[
    pytest.param(
        (TEST_EMAIL, TEST_PASSWORD, True),
        id='valid_email_and_password',
    ),
    pytest.param(
        (TEST_EMAIL, 'wrong_password', False),
        id='valid_email_wrong_password',
    ),
    pytest.param(
        ('test@gmail.com', TEST_PASSWORD, False),
        id='wrong_email_valid_password',
    ),
    pytest.param(
        ('test@gmail.com', '', False),
        id='valid_email_empty_password'
    ),
])
def password_validator_param(request):
    return request.param
