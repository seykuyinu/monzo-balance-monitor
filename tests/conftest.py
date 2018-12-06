import pytest
import os

# env var stubs
stub_monzo_api_url = "http://test.com"
os.environ['MONZO_API_URL'] = stub_monzo_api_url
os.environ['MONZO_AUTH_TOKEN'] = "123456789"

@pytest.fixture(scope='module')
def api_url():
    return stub_monzo_api_url

@pytest.fixture(scope='module')
def account_id():
    return "acc_XXXXXXXXXXX"