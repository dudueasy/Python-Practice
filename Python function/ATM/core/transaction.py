# -*- coding: utf-8 -*-
#__author__: 'Apolo Du'

from conf import settings
from core import accounts


def make_transaction(logger, account_data, tran_type, amount, target_user = None , **others):

    amount = float(amount)
    if tran_type in settings.TRANSACTION_TYPE:
        transaction_info = settings.TRANSACTION_TYPE[tran_type]
        interest = amount * transaction_info['interest']
        new_balance = ''

        old_balance = account_data['balance']
        if transaction_info['action'] == 'plus':
            new_balance = old_balance + amount + interest

        if transaction_info['action'] == 'minus':
            new_balance = old_balance - amount - interest
            if new_balance < 0:
                print('Your credit is not enough for this transaction')
                return

        account_data['balance'] = new_balance
        accounts.dump_account(account_data)
