#########creating json file for first time running:########
# import json
# with open('menu.json', 'w',encoding='utf-8') as f:
#     menu_data = json.dumps(menu)
#     f.write(menu_data)
#
# menu = {
#     '北京':{
#         '海淀':{
#             '五道口':{
#                 'soho':{},
#                 '网易':{},
#                 'google':{}
#             },
#             '中关村':{
#                 '爱奇艺':{},
#                 '汽车之家':{},
#                 'youku':{},
#             },
#             '上地':{
#                 '百度':{},
#             },
#         },
#         '昌平':{
#             '沙河':{
#                 '老男孩':{},
#                 '北航':{},
#             },
#             '天通苑':{},
#             '回龙观':{},
#         },
#         '朝阳':{},
#         '东城':{},
#     },
#     '上海':{
#         '闵行':{
#             "人民广场":{
#                 '炸鸡店':{}
#             }
#         },
#         '闸北':{
#             '火车战':{
#                 '携程':{}
#             }
#         },
#         '浦东':{},
#     },
#     '山东':{},
# }
######################################################

import json
with open('menu.json','r',encoding='utf-8') as menu_file:
    menu = json.load(menu_file)

#initiallize
# input_code = ''
cur_menu = menu
key_list = []


#functions
def get_input():
    show_info()
    input_code = input('请输入要进入的地区, 输入b返回上一级, 输入q退出程序: ')
    input_handler(input_code)

def show_info():
    if cur_menu:
        print('当前位置有以下地区: ')
        for i in cur_menu:
            print(i)
    else:
        print('已经进入最底层')

def input_handler(input_code):
    global key_list

    if input_code == '':
        print('输入为空!')
        get_input()

    elif input_code in cur_menu.keys():
        key_list.append(input_code)
        get_cur_menu(key_list)
        get_input()

    elif input_code == 'b':
        if key_list:
            key_list.pop()
            get_cur_menu(key_list)
            get_input()
        else:
            print("已经在最外层!")
            get_input()

    elif input_code == 'q':
        exit()
    else:
        print('请输入正确的地名!')
        get_input()


def get_cur_menu(list):
     global  cur_menu
     cur_menu = menu
     for each in list:
         cur_menu = cur_menu.get(each)

#execute
get_input()
