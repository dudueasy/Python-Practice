# -*- coding: utf-8 -*-
#__author__: 'Apolo Du'


def file_db_handler(connect_params):
    print('file db: ',connect_params)
    db_path = '%s/%s' %(connect_params['path'], connect_params['name'])
    return db_path

def mysql_db_handler(connect_params):
    pass

def db_handler(connect_params):
    if connect_params['engine'] == 'file_storage':
        return file_db_handler(connect_params)
    if connect_params['engine'] == 'mysql':
        return  mysql_db_handler(connect_params)