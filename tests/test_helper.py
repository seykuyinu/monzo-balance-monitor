import pytest
import json

from monzo_balance_monitor.helper import get_spending_pot_id, get_account_id, format_account_balance

class TestHelper(object):

    def test_get_spending_pot_id(self, shared_datadir):
        # Given
        pots_list = json.loads((shared_datadir / 'test_pots.json').read_text())
        pot_name = "Spending"
        expected_id = pots_list['pots'][2]['id']

        # When
        spending_pot_id = get_spending_pot_id(pots_list, pot_name)

        # Then
        assert spending_pot_id == expected_id

    def test_get_spending_pot_id_no_spending_pot(self, shared_datadir):
        # Given
        pots_list = json.loads((shared_datadir / 'test_pots.json').read_text())
        pot_name = "Spending"
        # remove spending pot
        del pots_list['pots'][2]

        # When
        spending_pot_id = get_spending_pot_id(pots_list, pot_name)

        # Then
        assert spending_pot_id == None

    def test_get_account_id(self, shared_datadir):
        # Given
        current_account = json.loads((shared_datadir / 'test_current_account.json').read_text())
        expected_account_id = current_account['accounts'][0]['id']

        # When
        account_id = get_account_id(current_account)

        # Then
        assert account_id == expected_account_id

    def test_format_account_balance(self):
        # Given
        test_scenarios = [
            (100, 1),
            (59, 0.59),
            (340000, 3400),
        ]

        for scenario in test_scenarios:
            balance = scenario[0]
            expected = scenario[1]

            # When
            formatted_balance = format_account_balance(balance)

            # Then
            assert formatted_balance == expected
