import pytest
import json

from monzo_balance_monitor.helper import get_spending_pot_id

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