# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
#
# 请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
#
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
#
#  
#
# 示例 1：
#
# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
# 示例 2：
#
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j][k]表示 前i个 中j个1  k个0的最大子集长度
        length = len(strs)
        # dp = [[[0 for _ in range(n+1)]for _ in range(m+1)] for _ in range(length+1)]
        # for i in range(1, length+1):
        #     cnt_1 = strs[i-1].count('1')
        #     cnt_0 = strs[i-1].count('0')
        #     for j in range(m+1):
        #         for k in range(n+1):
        #             dp[i][j][k] = dp[i-1][j][k]

        #             if j >= cnt_0 and k>=cnt_1:
        #                 dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-cnt_0][k-cnt_1] + 1)
        # return dp[-1][-1][-1]

        # 滚动数组
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, length + 1):
            cnt_1 = strs[i - 1].count('1')
            cnt_0 = strs[i - 1].count('0')
            for j in range(m, cnt_0 - 1, -1):
                for k in range(n, cnt_1 - 1, -1):
                    # dp[j][k] = dp[j][k]
                    # print(j, cnt_0, k, cnt_1)
                    # if j >= cnt_0 and k>=cnt_1:
                    # print(j,k,cnt_0, cnt_1)
                    dp[j][k] = max(dp[j][k], dp[j - cnt_0][k - cnt_1] + 1)
        return dp[-1][-1]


