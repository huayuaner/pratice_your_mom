# 给定一个字符串 s，返回 s 中不同的非空「回文子序列」个数 。
#
# 通过从 s 中删除 0 个或多个字符来获得子序列。
#
# 如果一个字符序列与它反转后的字符序列一致，那么它是「回文字符序列」。
#
# 如果有某个 i , 满足 ai != bi ，则两个序列 a1, a2, ... 和 b1, b2, ... 不同。
#
# 注意：
#
# 结果可能很大，你需要对 109 + 7 取模 。
#  
#
# 示例 1：
#
# 输入：s = 'bccb'
# 输出：6
# 解释：6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
# 注意：'bcb' 虽然出现两次但仅计数一次。
# 示例 2：
#
# 输入：s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
# 输出：104860361
# 解释：共有 3104860382 个不同的非空回文子序列，104860361 对 109 + 7 取模后的值。
#
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        # 三维数组
        # dp[x][i][j]表示 以字符x开头，下标为i:j（包含i,j）的个数
        # mod = 10**9+7
        # n = len(s)
        # dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(4)]
        # # 初始化，单个字符一定为回文
        # for i,c in enumerate(s):
        #     dp[ord(c)-ord('a')][i][i] = 1
        # # print(dp)
        # # 按对角线遍历
        # # 先从长度为2 遍历
        # for gap in range(2, n+1):
        #     for j in range(gap-1, n):
        #         i = j - gap + 1
        #         for idx, c in enumerate('abcd'):
        #             if s[i] ==c and s[j] == c:
        #                 # 如果首尾相同都为 c
        #                 # 中间所有情况 + 只有c 和 cc 两种情况
        #                 # 如果其中子串存在c和cc的情况，那么就会和新的头尾组合成 cc 和 cccc四种情况
        #                 dp[idx][i][j] = (2 + sum(d[i+1][j-1] for d in dp)) % mod
        #             elif s[i]==c:
        #                 # 为了保持 以 c 开头 所以是 [i][j-1]
        #                 # 以下同理
        #                 dp[idx][i][j] = dp[idx][i][j-1]
        #             elif s[j]==c:
        #                 dp[idx][i][j] = dp[idx][i+1][j]
        #             else:
        #                 dp[idx][i][j] = dp[idx][i+1][j-1]
        # # print(dp)
        # return sum(d[0][n-1] for d in dp)%mod

        # 二维数组
        mod = 10**9 + 7
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        pre_, next_ = [[0 for _ in range(4)] for _ in range(n)], [[0 for _ in range(4)] for _ in range(n)]
        pos = [-1] * 4
        # 建立pre_, next_数组
        # 可以从其中查找到位置i的字母c下一个和上一个相同字母的位置
        for i in range(n):
            for c in range(4):
                # print(i,c)
                pre_[i][c] = pos[c]
            pos[ord(s[i])-ord('a')] = i
        pos = [n] * 4
        for i in range(n-1,-1,-1):
            for c in range(4):
                next_[i][c] = pos[c]
            pos[ord(s[i])-ord('a')] = i
        # 初始化
        for i in range(n):
            dp[i][i] = 1
        for gap in range(2,n+1):
            for j in range(gap-1, n):
                i = j - gap + 1
                if s[i] == s[j]:
                    low, high = next_[i][ord(s[i])-ord('a')], pre_[j][ord(s[j])-ord('a')]
                    # 说明其中没有重复的头和尾 之前所有的回文首尾加上c就是新回文（2*dp[i+1][j-1]）再加上 c 和 cc两个
                    if low > high:
                        dp[i][j] = (2 + 2*dp[i+1][j-1])%mod
                    # 其中有一个，只有c这个重复了，删去
                    elif low == high:
                        dp[i][j] = (1 + 2*dp[i+1][j-1])%mod
                    # 其中存在重复的头尾c
                    # 那么dp[low][high]已经包含了 c 和 cc了  +2 删去
                    # 其中 dp[low+1][high-1]的内容首尾加c的内容重复，删去
                    else:
                        dp[i][j] = (2*dp[i+1][j-1] - dp[low+1][high-1])%mod
                else:
                    # 如果首尾不相同，就找两个区间的个数再减去重复区间的个数
                    dp[i][j] = (dp[i+1][j]+dp[i][j-1]- dp[i+1][j-1])%mod
        return dp[0][n-1]

