#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/10 13:02
# @Author  : daijianhao
# @File    : 直方图中最大的矩形.py
# 单调栈模板题

def process(nums: [int]):
    res = 0
    s = []
    for val in nums + [0]:
        if s:
            width = 0
            while s and val <= s[-1][0]:
                pop_item = s.pop()
                width += pop_item[-1]
                res = max(res, pop_item[0] * width)
            s.append((val, width + 1))
        else:
            s.append((val, 1))
    return res


in_str = input()
nums_list = []
while in_str[0] != "0":
    nums_list.append(list(map(int, in_str.split()[1:])))
    in_str = input()

for i in nums_list:
    print(process(i))
