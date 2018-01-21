# -*- coding: utf-8 -*-
#__author__: 'Apolo Du'

from . import auth
from . import logger
from core import accounts
from core import transaction


trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')


user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}


def account_info(acc_data):
    print(user_data)
    interactive(acc_data)


def repay(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])

    current_balance = '''------- BALANCE INFO --------
        Credit :  %s
        Balance:  %s'''%(account_data['credit'], account_data['balance'])
    print(current_balance)

    back_flag = False
    while not back_flag:
        repay_amount = input('Input repay amount, input q to go back: ').strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'repay',repay_amount)
        elif repay_amount == 'q':
            back_flag = True
        else:
            print('Invalid Amount!')

    user_data['account_data'] = accounts.load_current_balance(acc_data['account_id'])
    interactive(user_data)


def withdraw(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = '''------- BALANCE INFO --------
        Credit :  %s
        Balance:  %s'''%(account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input('input withdraw amount, input q to go back: ').strip()
        if len(withdraw_amount) >0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('New Balance: %s' % (new_balance['balance']))
        elif withdraw_amount == 'q':
            back_flag = True
        else:
            print('Invalid Amount!')

    user_data['account_data'] = accounts.load_current_balance(acc_data['account_id'])
    interactive(user_data)


def transfer(acc_data):
    pass

def pay_check(acc_data):
    pass

def logout(acc_data):
    exit()

def interactive(acc_data):

    menu = u'''
    ------ oldboy bank ------
    1. 账户信息
    2. 还款
    3. 取款
    4. 转账
    5. 账单
    6. 退出'''

    menu_dict = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }

    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input('>>:').strip()
        if user_option in menu_dict:
            menu_dict[user_option](acc_data)
        else:
            print('输入错误')


def run():
    acc_data = auth.acc_login(user_data, access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)
