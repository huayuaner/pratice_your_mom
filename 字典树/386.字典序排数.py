# 给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。
#
# 你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。
#
#  
#
# 示例 1：
#
# 输入：n = 13
# 输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]
# 示例 2：
#
# 输入：n = 2
# 输出：[1,2]
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # ans = [num for num in range(1,n+1)]
        # ans.sort(key = lambda x :str(x))
        # return ans

        ans = [0] * n
        num = 1
        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return ans