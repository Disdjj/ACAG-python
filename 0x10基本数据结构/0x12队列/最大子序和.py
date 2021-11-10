#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/10 13:31
# @Author  : daijianhao
# @File    : 最大子序和.py
n, m = map(int, input().split())
nums = list(map(int, input().split()))
pre_sum = [0]
for i in range(n):
    pre_sum.append(pre_sum[-1] + nums[i])

q = [0] * n
def process(nums: [int]):
    res = nums[0]
    q[1] = 0
    l, r = 1, 1
    for index, val in enumerate(nums, start=1):
        if l <= r and q[l] < index - m:
            l += 1
        res = max(res, pre_sum[index] - pre_sum[q[l]])
        while l <= r and pre_sum[q[r]] >= pre_sum[index]:
            r -= 1
        r += 1
        q[r] = index
    return res


def process_(nums: [int]):
    q = [0]
    res = nums[0]
    for index, val in enumerate(nums, start=1):
        if q and q[0] < index - m:
            q.pop(0)
        res = max(res, pre_sum[index] - pre_sum[q[0]])
        while q and pre_sum[q[-1]] >= pre_sum[index]:
            q.pop()
        q.append(index)
    return res


print(process(pre_sum[1:]))
