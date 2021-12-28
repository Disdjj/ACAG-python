# -*- coding: utf-8 -*-
'''
@author: DJJ
@e-mail: daijianhao@xiaobing.ai
@file: .py
@create time: 2021/12/28
@features: 
'''

SIZE = 1 << 20
heap = [None] * SIZE
index = 0


class Heap:
    def __init__(self):
        self.SIZE = 1 << 20
        self.heap = [0 for _ in range(SIZE)]
        self.index: int = 0

    def up(self, p):
        lst = self.heap
        while p > 1:
            if lst[p] > lst[p // 2]:
                lst[p], lst[p // 2] = lst[p // 2], lst[p]
                p //= 2
            else:
                break

    def down(self, p):
        lst = self.heap
        s = p * 2
        while s <= self.index:
            if s < self.index and lst[s] < lst[s + 1]:
                s += 1
            if lst[s] > lst[p]:
                lst[p], lst[s] = lst[s], lst[p]
                p = s
                s = 2 * p
            else:
                break

    def push(self, n: int) -> None:
        self.index += 1
        self.heap[self.index] = n
        self.up(self.index)

    def top(self) -> int:
        return self.heap[1]

    def pop(self):
        if self.index > 0:
            self.index -= 1
            self.heap[1] = self.heap[self.index]
            self.down(1)

    def remove(self, n):
        self.index -= 1
        self.heap[n] = self.heap[self.index]
        self.up(n)
        self.down(n)
