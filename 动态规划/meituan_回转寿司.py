# 小美请小团吃回转寿司。转盘上有N盘寿司围成一圈，第1盘与第2盘相邻，第2盘与第3盘相邻，…，第N-1盘与第N盘相邻，第N盘与第1盘相邻。
# 小团认为第i盘寿司的美味值为A[i]（可能是负值，如果小团讨厌这盘寿司）。现在，小团要在转盘上选出连续的若干盘寿司，使得这些寿司的美味值之和最大（允许不选任何寿司，此时美味值总和为0）。


# 思路
# 求常规最大和首位相连最大
# 常规最大就正常dp
# 首位相连最大就求常规最小和连续子序列，用总和一减就是首尾相连最大
# 取这两个最大中的更大值
T = int(input())
for _ in range(T):
    n = int(input())
    sushi = list(map(int, input().split()))
    max_dp = [0]*n
    min_dp = [0]*n
    max_dp[0] = min_dp[0] = sushi[0]
    max_val = float("-inf")
    min_val = float("inf")
    for i in range(1, n):
        max_dp[i] = max(max_dp[i-1]+sushi[i], sushi[i])
        min_dp[i] = min(min_dp[i-1]+sushi[i], sushi[i])
        max_val = max(max_val, max_dp[i])
        min_val = min(min_val, min_dp[i])
    print(max(max_val, sum(sushi)-min_val))