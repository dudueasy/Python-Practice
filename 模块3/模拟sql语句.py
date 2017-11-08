#
# # ---------------------initiallization---------------------
# user_info =[{'staff_id':1, 'name':'Alex Li', 'age':22, 'phone':13651054606,'dept':'IT','enroll_date':'2013-04-01'},
# {'staff_id':2, 'name':'Jack Wang', 'age':30, 'phone':13304320533,'dept':'HR','enroll_date':'2015-05-03'},
# {'staff_id':3, 'name':'Rain Liu', 'age':25, 'phone':1383235322,'dept':'Sales','enroll_date':'2016-04-22'},
# {'staff_id':4, 'name':'Mack Cao', 'age':40, 'phone':1356145343,'dept':'HR','enroll_date':'2009-03-01'}]
#
# import json
# with open('user_info.json','w') as file_obj:
#     json.dump(user_info,file_obj)
# # ---------------------initiallization--------------------

import json
import time

with open('user_info.json') as file_obj:
    user_info = json.load(file_obj)
    keywords = ['staff_id','name','age','phone','dept','enroll_date']

    def select():
        query_keywords = []
        result = []
        select_statm, condition = query_statm.split('where')
        key, operator, cmp_value = condition.split()
        operator = operator.strip()
        cmp_value = cmp_value.strip("\"")
        print(cmp_value)

        if '*' in select_statm:
            query_keywords = keywords

        else:
            for i in keywords:
                if i in select_statm:
                    query_keywords.append(i)

        if cmp_value.isdigit():
            cmp_value = int(cmp_value)

        for user in user_info:
            if operator == ">" and user[key] > cmp_value:
                result.append(user)
            if operator == '<' and user[key] < cmp_value:
                result.append(user)
            if operator == '='and user[key].lower() == cmp_value:
                result.append(user)
            if operator == 'like' and str(cmp_value) in user[key]:
                result.append(user)

        for user in result:
            msgs = []
            msg = ''
            for key_word in query_keywords:
                msg = "%s : %s "%(key_word, user[key_word])
                msgs.append(msg)
            print('| '.join(msgs))
        print('一共有 %d 条信息'%(len(result)))

    def insert():
        '''insert into table_name values (name, age, phone, dept)'''
        name, age, phone, dept = query_statm.split('(')[1].rstrip(')').split(',')

        if phone in user_info:
            print('phone number is not unique')
        else:
            localtime = time.localtime()
            date = time.strftime("%Y-%m-%d", localtime)
            user_info.append({'staff_id': len(user_info)+1, 'name':eval(name),
                              'age':eval(age),'phone':eval(phone),'dept':eval(dept.upper()),
                              'enroll_date':date})

    def delete():
        '''delete from table_name where key = value'''
        search, value = query_statm.split('where')[1].split('=')
        for user in user_info:
            if user[search.strip()].lower() == eval(value):
                user_info.remove(user)

    def update():
        '''update table SET key = value WHERE search = search value'''
        key, value = query_statm.split('set')[1].split('where')[0].split('=')
        search, search_value = query_statm.split('set')[1].split('where')[1].split('=')

        print(key, value, search, search_value)
        for user in user_info:
            print(user[search.strip().lower()])
            print(search_value.strip())
            if user[search.strip()].lower() == eval(search_value):
                print
                print('user found')
                user[str(key.strip())] = value.strip()

    query_statm = input('请输入查询语句: ').strip().lower()
    if query_statm.startswith('select'):
        select()
    if query_statm.startswith('insert into'):
        insert()
    if query_statm.startswith('delete'):
        delete()
    if query_statm.startswith('update'):
        update()

    for user in user_info:
        print(user)

    with open('user_info.json','w') as new_file:
            json.dump(user_info,new_file)
