import pytest
import responses
import requests
import json

from monzo_balance_monitor.monzo_api import get_current_account, get_account_balance, get_pots_list

class TestMonzoApi(object):
    
    @responses.activate 
    def test_get_current_account(self, shared_datadir, api_url):
        get_account_url = f"{api_url}/accounts?account_type=uk_retail"
        resp_body = (shared_datadir / 'test_current_account.json').read_text()

        responses.add(responses.Response(
            method='GET',
            url=get_account_url,
            match_querystring=True,
            status=200,
            json=resp_body
        ))

        response = get_current_account()
        assert response is not None
        assert response == resp_body

    @responses.activate
    def test_get_current_account_http_error(self, api_url):
        get_account_url = f"{api_url}/accounts?account_type=uk_retail"
        responses.add(responses.Response(
            method='GET',
            url=get_account_url,
            match_querystring=True,
            status=404
        ))

        with pytest.raises(requests.exceptions.HTTPError) as excinfo:
            get_current_account()


    @responses.activate
    def test_get_account_balance(self, shared_datadir, api_url, account_id):
        get_balance_url = f"{api_url}/balance?account_id={account_id}"
        resp_body = json.loads(
            (shared_datadir / 'test_balance.json').read_text())

        responses.add(responses.Response(
            method='GET',
            url=get_balance_url,
            match_querystring=True,
            status=200,
            json=resp_body
        ))

        response = get_account_balance(account_id)

        assert response is not None
        assert type(response) is int
        assert response == 1234

    @responses.activate
    def test_get_account_balance_http_error(self, api_url, account_id):
        get_balance_url = f"{api_url}/balance?account_id={account_id}"

        responses.add(responses.Response(
            method='GET',
            url=get_balance_url,
            match_querystring=True,
            status=500
        ))

        with pytest.raises(requests.exceptions.HTTPError) as excinfo:
            get_account_balance(account_id)

    @responses.activate
    def test_get_posts_list(self, shared_datadir, api_url):
        get_pots_list_url = f"{api_url}/pots"
        resp_body = json.loads(
            (shared_datadir / 'test_pots.json').read_text())

        responses.add(responses.Response(
            method='GET',
            url=get_pots_list_url,
            match_querystring=True,
            status=200,
            json=resp_body
        ))

        response = get_pots_list()

        assert response is not None
        assert response == resp_body

    @responses.activate
    def test_get_posts_list_http_error(self, api_url):
        get_pots_list_url = f"{api_url}/pots"

        responses.add(responses.Response(
            method='GET',
            url=get_pots_list_url,
            match_querystring=True,
            status=400
        ))

        with pytest.raises(requests.exceptions.HTTPError) as err:
            get_pots_list()
