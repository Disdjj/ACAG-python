#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 13:29
# @Author  : daijianhao
# @File    : 邻值查找.py
# From: https://www.acwing.com/problem/content/138/
n = int(input())
A = list(map(int, input().split()))


class Node:
    def __init__(self):
        self.l = None
        self.r = None
        self.val = None

    # def __repr__(self):
    #     return "val: {} \n".format(self.val)
    # 
    # def __str__(self):
    #     return "val: {} \n".format(self.val)


B = list(enumerate(A))
B.sort(key=lambda x: (x[-1], x[0]))
head = Node()
tail = Node()
head.r = tail
tail.l = head
now = head

for index, val in B:
    node = Node()
    node.val = (index, val)
    nxt = now.r
    node.l = now
    node.r = nxt
    now.r = node
    nxt.l = node
    A[index] = node
    now = now.r

res = []
for i in A[:0:-1]:
    l, r = i.l, i.r
    al = [(abs(x.val[-1] - i.val[-1]), x.val[1], x.val[0]) for x in (l, r) if x.val]
    al.sort()
    res.append(al[0][::2])

    nd = A[i.val[0]]
    lst, nxt = nd.l, nd.r
    lst.r = nxt
    nxt.l = lst
for a, b in res[::-1]:
    print("{} {}".format(a, b + 1))
