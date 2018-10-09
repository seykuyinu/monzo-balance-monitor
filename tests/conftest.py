import pytest

@pytest.fixture(scope='module')
def api_url():
    return "https://api.monzo.com"

@pytest.fixture(scope='module')
def account_id():
    return "acc_XXXXXXXXXXX"