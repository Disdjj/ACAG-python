Q = int(input())
reads = []

index_l = []
index_r = []
pre_s = [0] * 1000001
max_pre_s = [0] * 1000001


def update(now_index, num):
    if now_index == 0:
        pre_s[now_index] = num
        max_pre_s[now_index] = num
    else:
        pre_s[now_index] = pre_s[now_index - 1] + num
        max_pre_s[now_index] = max(max_pre_s[now_index - 1], pre_s[now_index])


res = []
for i in range(Q):
    s = input()
    now_index = len(index_l)
    if s[0] == "I":
        num = int(s.split()[-1])
        index_l.append(num)
        update(now_index, num)
    elif s[0] == "D":
        if index_l:
            index_l.pop()
    elif s[0] == "L":
        if index_l:
            item = index_l.pop()
            index_r.append(item)
    elif s[0] == "R":
        if index_r:
            item = index_r.pop()
            index_l.append(item)
            update(now_index, item)
    elif s[0] == "Q":
        num = int(s.split()[-1])
        res.append(max_pre_s[num - 1])
for i in res:
    print(i)
# print("over")
# exit()
