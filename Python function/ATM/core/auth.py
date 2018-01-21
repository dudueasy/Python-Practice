# -*- coding: utf-8 -*-
#__author__: 'Apolo Du'
import os, time, json
from conf import settings
from core import db_handler


def acc_auth(account, password):

    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = '%s/%s.json' %(db_path, account)
    print(account_file)

    if os.path.isfile(account_file):
        with open(account_file, 'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                print('welcome')
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'],'%Y-%m-%d'))
                if time.time() > exp_time_stamp:
                    print('account has been expired, please contact the administrator')

                else:
                    return account_data
            else:
                print('Account ID or password is incorrect')
    else:
        print('Account does not exist')




def acc_login(user_data, logger):

    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input('account: ').strip()
        password = input('password: ').strip()
        auth = acc_auth(account, password)

        #结果不为空.
        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            print('welcome')
            return auth

        retry_count += 1
    else:
        logger.error('account: [%s] too many attempts' % account)
        exit()
