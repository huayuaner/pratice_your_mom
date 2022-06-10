# 有 N 种物品和一个容量是 V 的背包。
#
# 第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
#
# 求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
# 输出最大价值。
#
# 输入格式
# 第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
#
# 接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。
#
# 输出格式
# 输出一个整数，表示最大价值。
#
# 数据范围
# 0<N,V≤100
# 0<vi,wi,si≤100

'''
dp[j]  总体积是j的情况下的最大价值

for i in range(n):
    for j in range(m,-1,-1):
        k = 0
        while k*v[i]<j:
            dp[j] = max(dp[j], dp[j-k*v[i]] + k*w[i])
            k += 1


'''
import sys

n, m = map(int, sys.stdin.readline().split())
dp = [0] * (m + 1)
for i in range(n):
    v, w, s = map(int, sys.stdin.readline().split())
    for j in range(m, -1, -1):
        for k in range(1, s + 1):
            if k * v <= j:
                dp[j] = max(dp[j], dp[j - k * v] + k * w)
            else:
                break
print(dp[-1])