#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 13:13
# @Author  : daijianhao
# @File    : 64位整数乘法.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/4 11:19
# @Author  : daijianhao
# @File    : a^b.py

def mul_64(a, b, p):
    res = 0
    while b != 0:
        if b & 1 == 1:
            res = (res + a) % p
        b = b >> 1
        a = (a * 2) % p
    return res % p


# 3 2 7
a = int(input())
b = int(input())
p = int(input())
print(mul_64(a, b, p))
