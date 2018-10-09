# Python wrapper for Monzo api

import os
import requests
import logging
from monzo_balance_monitor.helper import get_account_id
from monzo_balance_monitor.helper import get_spending_pot_id

api_url = os.environ['MONZO_API_URL']
auth_token = os.environ['MONZO_AUTH_TOKEN']
current_account_type = "uk_retail"
headers = {"authorization": f"Bearer {auth_token}"}

def get_current_account():
    """
        Returns the current account associated with the given user account.
    """
    url = f"{api_url}/accounts"
    params = {'account_type': current_account_type}

    response = requests.get(url=url, params=params, headers=headers)

    response.raise_for_status()

    return response.json()


def get_account_balance(account_id):
    """
        Returns the balance of the account matching the given account id

        Keyword arguments:
        account_id - id of the account to retrieve balance
    """
    url = f"{api_url}/balance"
    params = {'account_id': account_id}

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    account_balance = response.json().get('balance')

    return account_balance


def get_pots_list():
    """
        Returns the list of pots associated with the given user account.
    """

    url = f"{api_url}/pots"

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()
