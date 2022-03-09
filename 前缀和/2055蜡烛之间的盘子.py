# 给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 s ，它只包含字符 '*' 和 '|' ，其中 '*' 表示一个 盘子 ，'|' 表示一支 蜡烛 。
#
# 同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] 表示 子字符串 s[lefti...righti] （包含左右端点的字符）。对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。如果一个盘子在 子字符串中 左边和右边 都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。
#
# 比方说，s = "||**||**|*" ，查询 [3, 8] ，表示的是子字符串 "*||**|" 。子字符串中在两支蜡烛之间的盘子数目为 2 ，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
# 请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        #动态规划 + 前缀和
        n = len(s)
        # 记录每个位置的前缀和，记录每个位置左边第一个蜡烛位置，记录每个位置右边第一个蜡烛位置
        presum, left, right = [0] * (n+1), [-1]*n, [-1]*n
        l = -1
        for idx,c in enumerate(s):
            if c == '*':
                presum[idx+1] = presum[idx] + 1
            else:
                presum[idx+1] = presum[idx]
                # 记录遇到蜡烛的位置
                l = idx
            # 在遇到下一个蜡烛之前的点的左边最近蜡烛都是i
            left[idx] = l
        r = -1
        for idx,c in enumerate(s[::-1]):
            if c == '|':
                r = n-1-idx
            right[n-1-idx] = r
        return [presum[left[r]] - presum[right[l]] if left[r]>=0 and right[l]>=0 and left[r]>right[l]  else 0 for l,r in queries]
