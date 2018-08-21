# Python wrapper for Monzo api
import os
import requests
# from monzo_balance_monitor.log_http import log_request
import logging
from monzo_balance_monitor.helper import get_account_id
from monzo_balance_monitor.helper import get_spending_pot_id

# IN CONFIG?
API_URL = "https://api.monzo.com"

current_account_type = "uk_retail"

auth_token = os.environ['MONZO_AUTH_TOKEN']

headers = {"authorization": f"Bearer {auth_token}"}

# TODO: error handling for the non-200 codes!
# wrapper for requests? otherwise duplicating error handling!


def get_current_account():
    url = f"{API_URL}/accounts"
    params = {'account_type': current_account_type}
    # log_request(url,"GET",headers)
    response = requests.get(url=url, params=params, headers=headers)

    # unit test this does what you want
    response.raise_for_status()

    return response.json()


def get_account_balance(account_id):
    """
        Returns the balance of the account matching the given account id
    """
    url = f"{API_URL}/balance"
    params = {'account_id': account_id}
    # log_request(url,"GET",headers)
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    account_balance = response.json().get('balance')

    return account_balance


def get_pots_list():
    url = f"{API_URL}/pots"
    # log_request(url,"GET",headers)
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()


# def withdraw_from_pot():
#     url = 

if __name__ == "__main__":
    pots_list = get_pots_list()
    get_spending_pot_id(pots_list)