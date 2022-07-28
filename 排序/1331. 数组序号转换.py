# 给你一个整数数组 arr ，请你将数组中的每个元素替换为它们排序后的序号。
#
# 序号代表了一个元素有多大。序号编号的规则如下：
#
# 序号从 1 开始编号。
# 一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
# 每个数字的序号都应该尽可能地小。
#
import heapq


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # helper = []
        # n = len(arr)
        # for i,num in enumerate(arr):
        #     helper.append((num, i))
        # ans = [0]*n
        # helper.sort()
        # pre = float('inf')
        # newidx = -1
        # for (num,i) in helper:
        #     if num != pre:
        #         newidx += 1
        #         pre = num

        #     ans[i] = newidx+1
        # return ans

        dic = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [dic[num] for num in arr]
