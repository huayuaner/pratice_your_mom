# 有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
#
# 第 i 件物品的体积是 vi，价值是 wi。
#
# 求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
# 输出最大价值。
#
# 输入格式
# 第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。
#
# 接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。
#
# 输出格式
# 输出一个整数，表示最大价值。
#
# 数据范围
# 0<N,V≤1000
# 0<vi,wi≤100

import sys

n, Vol = map(int, sys.stdin.readline().split())
vols, vals = [], []
# for _ in range(n):
#     vol, val = map(int, sys.stdin.readline().split())
#     vols.append(vol)
#     vals.append(val)

# print(vv)
'''
dp[i][j] 表示 前i个物品，总体积是j的情况下，最大的总价值
ans = max(dp[n][0~V])
dp[i][j]
1. 不选第i个物品，dp[i][j] = dp[i-1][j]
2. 选第i个物品， dp[i][j] = dp[i-1][j-v[i]]
dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[i]]) + val[i]

dp[0][0] = 0

复杂度 N*V
'''
# dp = [[0 for _ in range(Vol+1)] for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(Vol+1):
#         if j < vols[i-1]:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-vols[i-1]]+vals[i-1])

# 滚动数组
dp = [0] * (Vol + 1)
for i in range(1, n + 1):
    v, w = map(int, sys.stdin.readline().split())
    # 从后往前，防止dp[i-1][j-vols[i-1]]已经被替代的情况
    for j in range(Vol, v - 1, -1):
        # if j >= vols[i-1]:
        dp[j] = max(dp[j], dp[j - v] + w)
'''
体积恰好是Vol的情况下的最大价值，该怎么做
dp[0] = 0
dp[i] = float("-inf")
这样可以确保dp[-1]一定是从dp[0][0]转移过来的，因为从其他状态转移的都是负无穷
'''

print(dp[-1])