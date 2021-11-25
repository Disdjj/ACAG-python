#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/25 13:23
# @Author  : daijianhao
# @File    : 动态中位数.py
import heapq

P = int(input())


class Node:
    def __init__(self):
        self.l = None
        self.r = None
        self.val = None
        self.index = None

    def __repr__(self):
        return "val: {} \n".format(self.val)

    def __str__(self):
        return "val: {} \n".format(self.val)


def process_1(nums: [int]) -> [int]:
    """
    linked list
    """
    sort_nums = sorted(list(enumerate(nums)), key=lambda x: (x[1], x[0]))
    node_list = [0] * len(nums)
    head = Node()
    tail = Node()
    head.r = tail
    tail.l = head
    now = head
    for sor_index, (index, val) in enumerate(sort_nums):
        node = Node()
        node.val = val
        node.index = sor_index
        nxt = now.r
        node.l = now
        node.r = nxt
        now.r = node
        nxt.l = node
        now = now.r
        node_list[index] = node
    now_len = len(nums)
    mid = node_list[sort_nums[(now_len - 1) // 2][0]]
    res = []
    while now_len > 0:
        x = nums[now_len - 1]
        delete = node_list[now_len - 1]
        mid_num = mid.val
        if now_len % 2 == 1:
            res.append(mid_num)
            if delete.index >= mid.index:
                mid = mid.l
        else:
            if delete.index <= mid.index:
                mid = mid.r
        lst = delete.l
        nxt = delete.r
        lst.r = nxt
        nxt.l = lst
        now_len -= 1
    return res[::-1]


def process_2(nums: [int]) -> [int]:
    res = []
    big = []
    small = []

    def balance():
        while len(big) > len(small) + 1:
            item = heapq.heappop(big)
            heapq.heappush(small, -item)
        while len(small) > len(big):
            item = heapq.heappop(small)
            heapq.heappush(big, -item)

    for index, val in enumerate(nums):
        if big:
            last_mid = -big[0]
        else:
            last_mid = nums[0]
        if val > last_mid:
            heapq.heappush(small, val)
        else:
            heapq.heappush(big, -val)
        balance()
        if index % 2 == 0:
            res.append(-big[0])
    return res


res = []
for i in range(P):
    n_, M = map(int, input().split())
    nums = []
    while len(nums) < M:
        nums.extend(list(map(int, input().split())))
    res.append(process_2(nums))

for index, val in enumerate(res):
    print("{} {}".format(index + 1, len(val)))


    def p(nums: [int]):
        print(" ".join(map(str, nums)))


    while len(val) > 10:
        p(val[:10])
        val = val[10:]
    else:
        p(val)
