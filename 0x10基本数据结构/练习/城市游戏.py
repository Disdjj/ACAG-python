# 单调栈
N, M = map(int, input().split())
l = []
for x in range(N):
    l.append(list(input().strip().split()))

pre_l = []

for index, val in enumerate(l):
    if index == 0:
        pre_l.append([0 if i == "R" else 1 for i in l[0]])
    else:
        next_l = []
        for j in range(M):
            last_v = pre_l[index - 1][j]
            now = 0 if val[j] == "R" else 1
            if last_v != 0:
                next_l.append(last_v + now)
            else:
                next_l.append(now)
        pre_l.append(next_l)


def process(nums: [int]):
    s = []
    res = 0
    for val in nums + [0]:
        if not s:
            s.append((1, val))
        else:
            wid = 0
            while s and s[-1][-1] >= val:
                w, h = s.pop()
                wid += w
                res = max(res, wid * h)
            s.append((wid + 1, val))
    return res


res = 0
for i in pre_l:
    res = max(res, process([x if x > 0 else 0 for x in i]))
    # res = max(res, process([-x if x < 0 else 0 for x in i]))

print(3 * res)
