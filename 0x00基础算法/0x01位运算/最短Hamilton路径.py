# -*- coding: utf-8 -*-
n = int(input())
dis_map = []
for i in range(n):
    dis_map.append(list(map(int, input().split())))

dp = [[1 << 30] * 20 for i in range(1 << 20)]
dp[1][0] = 0
for i in range(1, 1 << n):
    for j in range(n):
        if (i >> j) & 1 == 1:
            for k in range(n):
                last_status = i ^ (1 << j)
                if last_status >> k & 1 == 1:
                    dp[i][j] = min(dp[i][j], dp[last_status][k] + dis_map[k][j])

print(dp[(1 << n) - 1][n - 1])
