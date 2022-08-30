# 给你两个下标从 0 开始的整数数组 nums 和 removeQueries ，两者长度都为 n 。对于第 i 个查询，nums 中位于下标 removeQueries[i] 处的元素被删除，将 nums 分割成更小的子段。
#
# 一个 子段 是 nums 中连续 正 整数形成的序列。子段和 是子段中所有元素的和。
#
# 请你返回一个长度为 n 的整数数组 answer ，其中 answer[i]是第 i 次删除操作以后的 最大 子段和。
#
# 注意：一个下标至多只会被删除一次。
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        # 为什么倒着想更容易
        # 加入数字后可以合并往左合并往右合并，或者把左右两段给合并了
        # 并查集
        n = len(nums)
        father = list(range(n+1))
        tot = [0]*(n+1)
        def find(x):
            if father[x] != x:
                father[x] = find(father[x])
            return father[x]
        ans = [0]*n
        for i in range(n-1, 0, -1):
            x = removeQueries[i]
            # 因为长度father 和 tot长度是 N+1
            to = find(x+1)
            father[x] = to # 合并 x, x+1
            tot[to] += tot[x] + nums[x]
            ans[i-1] = max(ans[i], tot[to])
        # print(tot,father)
        return ans
