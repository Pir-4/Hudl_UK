import pytest

@pytest.fixture(params=[
    pytest.param(('test@test.com', True), id='valid'),
    pytest.param(('Test@Test.com', True), id='capitalize'),
    pytest.param(('test-4@test.com', True), id='number_and_punctuation'),
    pytest.param(('my.te4st-t@lk.c.com.net', True), id='complex'),
    pytest.param(
        ('xn--_@-wlcbbeejdu5d6bnh3g.xn--p1ai', False), id='punnycode'
    ),
    pytest.param(('мой_ящик@лучший.рф', False), id='local_lang'),
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
