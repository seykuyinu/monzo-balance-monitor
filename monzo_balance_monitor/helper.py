# Helper functions to process Monzo data objects

def get_spending_pot_id(pots_dict, pot_name):
    pots_list = pots_dict.get('pots')

    spending_pot = list(filter(lambda pot: pot['name'].strip() == pot_name, pots_list))
    if len(spending_pot) != 1:
        # TODO: error? or just log?
        return None
    else:
        return spending_pot[0]['id']

def get_account_id(accounts):
    # assumes only one current account
    account = accounts.get('accounts')[0]

    return account['id']

def format_account_balance(balance):
    return balance / 100
