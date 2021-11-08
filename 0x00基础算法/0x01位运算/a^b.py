#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/4 11:19
# @Author  : daijianhao
# @File    : a^b.py

def power(a, b, p):
    res = 1 % p
    while b != 0:
        if b & 1 == 1:
            res *= (a % p)
        b = b >> 1
        a = (a * a) % p
    return res % p


# 3 2 7
a, b, p = map(int, input().split())
print(power(a, b, p))
