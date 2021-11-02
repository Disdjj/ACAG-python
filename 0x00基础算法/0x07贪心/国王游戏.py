n = int(input())
king_l, king_r = map(int, input().split())
persons = []
for i in range(n):
    persons.append(tuple(map(int, input().split())))
persons.sort(key=lambda x: x[0] * x[1])
pre = []
for i in range(n):
    if i == 0:
        pre.append(king_l)
    else:
        pre.append(pre[-1] * persons[i - 1][0])
res = 0
for index, item in enumerate(pre):
    res = max(res, item // persons[index][1])
print(res)
