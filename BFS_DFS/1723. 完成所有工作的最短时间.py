# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
#
# 请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
#
# 返回分配方案中尽可能 最小 的 最大工作时间 。
#
#  
#
# 示例 1：
#
# 输入：jobs = [3,2,3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。
# 示例 2：
#
# 输入：jobs = [1,2,4,7,8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）
# 最大工作时间是 11 。
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # 二分 + dfs
        # 从小到大排序，这样不合法的话可以更快跳出
        # arr  = sorted(jobs)
        # def check(limit):

        #     group = [0]*k
        #     if dfs(arr, group, limit):
        #         return True
        #     else:
        #         return False
        # def dfs(arr, group, limit):
        #     # print(group)
        #     if not arr:
        #         return True
        #     # 每次弹出最后一个
        #     job = arr.pop()
        #     # 遍历出分配的所有情况
        #     for i in range(k):
        #         # 只有job<=limit才能放
        #         if group[i] + job <= limit:
        #             group[i] += job
        #             if dfs(arr,group, limit):
        #                 arr.append(job)
        #                 return True
        #             group[i] -= job
        #             # 如果一个工作在第i个人完全没有工作的情况下都不能合法分配，那么该人有工作的情况更不可能合法分配
        #             # 所以直接跳出
        #             if group[i] == 0:
        #                 break
        #     arr.append(job)
        #     return False
        # # print(check(11))
        # l,r = max(jobs), sum(jobs)
        # while l<r:
        #     m = l + (r-l)//2
        #     # print(arr)
        #     if check(m):
        #         r = m
        #     else:
        #         l = m + 1
        #     # print(l,m, r)
        # return l
        m = len(jobs)
        n = 2 ** m
        # 先计算sum(j)
        dict_sum = defaultdict(int)
        for j in range(1, n):
            for i in range(m):
                # print(j,2**i)
                if j & (1 << i): dict_sum[j] += jobs[i]
                # dp[i][j]表示前[:i+1]个人处理子集j的最短工作时间
        dp = [[float('inf')] * (n) for _ in range(k)]
        # 初始化，当只有0号工人，其承担所有工作
        for j in range(n):
            dp[0][j] = dict_sum[j]
        ans = dict_sum[n - 1]
        for i in range(1, k):
            for j in range(n):
                # 获得j的所有子集
                subset_j = self.subset(j)
                # print(j, subset_j)
                if len(subset_j) > 0:
                    # 这里max里的内容是i-1个人承担j^j1的工作，第i个人承担j1的工作，计算两者较大值
                    # 在左右子集情况中取得最小值
                    dp[i][j] = min([max(dp[i - 1][j ^ j1], dict_sum[j1]) for j1 in subset_j])
        ans = min(ans, dp[-1][-1])
        return ans

    def subset(self, j):
        # print(j)
        res = []
        j1 = (j - 1) & j
        while j1 > 0:
            res.append(j1)
            j1 = (j1 - 1) & j
        # print(res)
        return res



