#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

# source = '1*22+(5+2)*3'
source = input('请输入计算式')

# 检查输入是否合法
def check(s):
    flag = True
    if re.findall(r'[^0-9\+\-\*\/\s\(\)]',s):
        print('包含非法字符')
        flag = False

    if s.count('(') != s.count(')'):
        print('括号未闭合')
        flag = False

    return flag


# 格式化字符串
def formatter(s):
    s = re.sub('\s','',s)
    s = re.sub(r'(\+\+|\-\-)', '+', s)
    s = re.sub(r'(\+\-|\-\+)','-',s)
    return s


# 计算
def calculate(s):
    #计算乘除
    if re.search('^\(.*\)$',s):
        s = s.lstrip('(').rstrip(')')

    result = re.search('\d+\.?\d*[*/]\d+\.?\d*',s)
    while result:
        expression = result.group()
        num_1,num_2 = re.split('[*/]',expression)
        num_1 = float(num_1)
        num_2 = float(num_2)
        if '*' in expression:
            res =  str(num_1* num_2)
        if '/' in expression:
            res =  str(num_1/num_2)
        s = s.replace(expression, res)
        result = re.search('\d+\.?\d*[*/]\d+\.?\d*', s)

    else:
        # 计算加减法
        result = re.search('\d+\.?\d*[+-]\d+\.?\d*', s)
        while result:
            expression = result.group()
            num_1,num_2 = re.split('[+-]',expression)
            num_1 = float(num_1)
            num_2 = float(num_2)
            if '+' in expression:
                res = str(num_1 + num_2)
            if '-' in expression:
                res = str(num_1 - num_2)
            s = s.replace(expression, res)
            result = re.search('\d+\.?\d*[+-]\d+\.?\d*', s)

    # 返回计算结果
    return s


if check(source):
    source = formatter(source)
    while re.search('\(',source):
        num_string = re.search('\([^()]+\)',source).group()
        source = source.replace(num_string,calculate(num_string))
    else:
        source = calculate(source)

print(source)
