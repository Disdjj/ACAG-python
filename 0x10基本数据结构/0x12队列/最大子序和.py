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


def process(nums: [int]):
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
