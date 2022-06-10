# 有 N 种物品和一个容量是 V 的背包，每种物品都有无限件可用。
#
# 第 i 种物品的体积是 vi，价值是 wi。
#
# 求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
# 输出最大价值。
#
# 输入格式
# 第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
#
# 接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 种物品的体积和价值。
#
# 输出格式
# 输出一个整数，表示最大价值。
#
# 数据范围
# 0<N,V≤1000
# 0<vi,wi≤1000

# 完全背包问题：物品可以无限次选择
import sys

n, m = map(int, sys.stdin.readline().split())
vols, vals = [], []
# for _ in range(n):
#     vol, val = map(int, sys.stdin.readline().split())
#     vols.append(vol)
#     vals.append(val)
'''
dp[j] 表示 体积是j的情况下，最大价值是多少

for i in range(1,n+1):
    for j in range(m, -1, -1):
        # 第i个物品拿k次
        k = 0
        # 选择最大，直到拿超
        while k*vols[i] <=j：
            dp[j] = max(dp[j], f[j-k*v[i-1]]+k*vals[i-1])

可以简化成
for i in range(1,n+1):
    for j in range(m+1):
        if j>= vols[i-1]:
            # 之前从后往前是为了选的dp[j-vols[i-1]] + vals[i-1]是不包含第i个物品
            # 但是当物品i无限次选择的时候，dp[j-vols[i-1]] + vals[i-1]已经包含了若干次i物品，和上面第i个物品拿k次相同
            dp[j] = max(dp[j], dp[j-vols[i-1]] + vals[i-1])

'''
# dp = [0]*(m+1)
# for i in range(n):
#     for j in range(1, m+1):
#         if j>=vols[i]:
#             dp[j] = max(dp[j], dp[j-vols[i]] + vals[i])
# print(dp[-1])

# 一遍获取输入一边更新
dp = [0] * (m + 1)
for i in range(n):

    v, w = map(int, sys.stdin.readline().split())
    for j in range(v, m + 1):
        dp[j] = max(dp[j], dp[j - v] + w)
print(dp[-1])
