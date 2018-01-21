# -*- coding: utf-8 -*-
#__author__: 'Apolo Du'

import os

import json

user_info = {
    'id':'apolo11',
    'password': '11111111',
    'credit': 15000,
    'balance': 15000,
    'enroll_date':'2017-01-01',
    'expire_date':'2022-01-01',
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}

with open(os.path.join('accounts',user_info['id']+'.json'),'w') as file_obj:

    json.dump(user_info,file_obj)
