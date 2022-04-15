# 给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
# 输出需要删除的字符个数。
# 思路
# 就是找s和s逆序的最长公共子序列
def helper(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


while 1:
    try:

        s1 = input().strip()
        s2 = s1[::-1]
        print(len(s1) - helper(s1, s2))
    except:
        break