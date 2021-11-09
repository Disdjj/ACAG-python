# 注意行列的对应情况

start_str = input() + input() + input() + input()
start = 0
for index, val in enumerate(start_str):
    if val == "+":
        start = start | (1 << index)
all_status = 1 << 16
min_op_num = 16
min_op = 0
pre = [0] * 16
for i in range(16):
    res = 0
    x, y = i // 4, i % 4
    for j in range(0, 4):
        res += 1 << (4 * j + y)
        res += 1 << (4 * x + j)
    res -= 1 << i
    pre[i] = res


def count_1(n):
    res = 0
    while n != 0:
        res += 1
        n -= (n & (-n))
    return res


for op in range(all_status):
    another_op = 0
    for i in range(16):
        if (op >> i) & 1 == 1:
            another_op ^= pre[i]
    if start - another_op == 0:
        if count_1(op) <= min_op_num:
            min_op_num = count_1(op)
            min_op = op

print(min_op_num)
for i in range(16):
    if min_op >> i & 1 == 1:
        x, y = i // 4, i % 4
        print("{} {}".format(x + 1, y + 1))
