# -*- coding: utf-8 -*-
def cal_next(a: str):
    next_list = [0] * len(a)
    for i in range(1, len(a)):
        j = next_list[i - 1]
        while j > 0 and a[i] != a[j]:
            j = next_list[j]
        if a[i] == a[j]:
            j += 1
        next_list[i] = j
    return next_list


def kmp(a: str, b: str):
    next_list = cal_next(a)
    f = [0] * len(b)
    for i in range(len(b)):
        j = f[i - 1]
        while j > 0 and (j == len(a) or b[i] != a[j]):
            j = next_list[j]
        if b[i] == a[j]:
            j += 1
        f[i] = j
        if j == len(a):
            return True
    else:
        return False
