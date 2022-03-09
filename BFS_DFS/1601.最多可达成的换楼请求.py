# 我们有 n 栋楼，编号从 0 到 n - 1 。每栋楼有若干员工。由于现在是换楼的季节，部分员工想要换一栋楼居住。
#
# 给你一个数组 requests ，其中 requests[i] = [fromi, toi] ，表示一个员工请求从编号为 fromi 的楼搬到编号为 toi 的楼。
#
# 一开始 所有楼都是满的，所以从请求列表中选出的若干个请求是可行的需要满足 每栋楼员工净变化为 0 。意思是每栋楼 离开 的员工数目 等于 该楼 搬入 的员工数数目。比方说 n = 3 且两个员工要离开楼 0 ，一个员工要离开楼 1 ，一个员工要离开楼 2 ，如果该请求列表可行，应该要有两个员工搬入楼 0 ，一个员工搬入楼 1 ，一个员工搬入楼 2 。
#
# 请你从原请求列表中选出若干个请求，使得它们是一个可行的请求列表，并返回所有可行列表中最大请求数目。
#
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # 暴力枚举
        # dfs + 回溯
        # 计算各栋楼是否为0
        # cnt = [0] * n
        # def dfs(pos, n):
        #     if pos == len(requests):
        #         for c in cnt:
        #             if c!=0:
        #                 return 0
        #         return n
        #     #搬出
        #     cnt[requests[pos][0]] -= 1
        #     # 搬入
        #     cnt[requests[pos][1]] += 1
        #     # pos位置选，选择cnt才会有变化
        #     ans = dfs(pos+1, n+1)
        #     # 回溯复原

        #     cnt[requests[pos][0]] += 1

        #     cnt[requests[pos][1]] -= 1
        #     # 返回该位置选和不选的最大值
        #     return max(ans, dfs(pos+1, n))
        # return dfs(0,0)

        # 二进制枚举
        ans = 0
        for i in range(1 << len(requests)):
            # 记录选了几个request
            cnt = i.bit_count()
            if cnt < ans:
                continue
            count = [0] * n
            for j, request in enumerate(requests):
                if (1 << j) & i:
                    count[request[0]] -= 1
                    count[request[1]] += 1
            if all(x == 0 for x in count):
                ans = cnt
        return ans


