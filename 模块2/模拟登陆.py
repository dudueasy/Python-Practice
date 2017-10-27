################## code for first time running:################
# userinfo = {'apolo':{'password':'password','locked':0},
#             'Logan':{'password':'x-man','locked':0},
#             'locked_user':{'password':'xyz','locked':1} }
# import json
# with open('userinfo.json','w') as userfile:
#     json.dump(userinfo,userfile)
##############################################################

import json

with open('userinfo.json','r') as userfile:
    userinfo = json.load(userfile)
    import getpass
    #initiallize
    count = 0
    user_nofound = True

    while user_nofound:
        username = input('请输入用户名: ').strip()

        if username in userinfo.keys():

            if userinfo[username]['locked'] == 1:
                print('this user is locked')
                continue

            user_nofound = False
            while count < 3 :
                password = getpass.getpass('请输入用户密码: ').strip()
                if userinfo[username]['password'] != password :
                    print('wrong password!\n')
                    count += 1
                    continue

                else:
                    print('welcome back '+username)
                    exit(0)

            else:
                userinfo[username]['locked'] = 1
                print(username + ' locked')

        else:
            print('user not found!')
            user_nofound = True

with open('userinfo.json','w') as userfile:
    json.dump(userinfo,userfile)
