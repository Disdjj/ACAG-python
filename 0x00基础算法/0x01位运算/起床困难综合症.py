# 起床困难综合征
# 00000000000
# 11111111111
# 每一位之间都没有联系
# 即每一位都有最优解, 用0000, 1111 来测试可以完成对所有情况的遍历, 从高位开始, 选择伤害最大, 且不会超过m的位
n, m = map(int, input().split())
op_list = []
or_func = lambda a, b: a | b
xor_func = lambda a, b: a ^ b
and_func = lambda a, b: a & b
for i in range(n):
    op, num = input().split(" ")
    func = and_func
    num = int(num)
    if op == "OR":
        func = or_func
    elif op == "XOR":
        func = xor_func
    op_list.append([func, num])


def process(n):
    for op, num in op_list:
        n = op(n, num)
    return n


num_0 = process(0)
num_1 = process((1 << 32) - 1)

res = 0
index = 0
for i in range(30):
    num0_i = (num_0 >> i) & 1
    num1_i = (num_1 >> i) & 1
    if num0_i < num1_i and index + (1 << i) <= m:
        res += (num1_i << i)
        index += (1 << i)
    else:
        res += num0_i << i
print(res)
