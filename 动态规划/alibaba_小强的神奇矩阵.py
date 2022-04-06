# 小强有一个3*n的矩阵，
# 他将中每列的三个数字中取出一个按顺序组成一个长度为n的数组，
# 求这个序列前-后的绝对值的和的最小值
# 动态规划
def dp(marix, n):
    # 初始dp
    dp = [0, 0, 0]
    for j in range(1, n):
        delta = []
        # 第i个把前面三个都减一遍再加上前面的和
        for i in range(3):
            d0 = abs(marix[i][j] - marix[0][j - 1]) + dp[0]
            d1 = abs(marix[i][j] - marix[1][j - 1]) + dp[1]
            d2 = abs(marix[i][j] - marix[2][j - 1]) + dp[2]
            # 得到第i行能得到的最小值
            delta.append(min(d0, d1, d2))
        # 更新动态规划矩阵
        dp = delta
    print(min(dp))
    return


col = int(input())
matrix = []
for _ in range(3):
    matrix.append(list(map(int, input().split())))
dp(matrix, col)
