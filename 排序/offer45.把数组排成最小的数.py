# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
#
#  
#
# 示例 1:
#
# 输入: [10,2]
# 输出: "102"
# 示例 2:
#
# 输入: [3,30,34,5,9]
# 输出: "3033459"

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        # 快速排序
        # def quick_sort(l, r):
        #     if l >= r:
        #         return
        #     i,j = l, r
        #     while i<j:
        #         while strs[j]+strs[l] >= strs[l] + strs[j] and i < j : j-=1
        #         while strs[l] + strs[i] >= strs[i] + strs[l] and i < j : i += 1
        #         #print(i,j)
        #         strs[i], strs[j] = strs[j], strs[i]
        #     strs[i], strs[l] = strs[l], strs[i]
        #     quick_sort(l, i-1)
        #     quick_sort(i+1, r)
        # strs = [str(num) for num in nums]
        # quick_sort(0,len(strs)-1)
        # return ''.join(strs)

        # API
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)

