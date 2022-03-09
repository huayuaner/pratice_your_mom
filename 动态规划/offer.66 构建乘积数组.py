# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
#
#  
#
# 示例:
#
# 输入: [1,2,3,4,5]
# 输出: [120,60,40,30,24]

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        # 动态规划
        # n = len(a)
        # # tmp存每个位置左边的乘积
        # l = [1] * n
        # for i in range(1, n):
        #     l[i] = a[i-1]*l[i-1]
        # r = [1] * n
        # for i in range(n-2,-1,-1):
        #     r[i] = a[i+1]*r[i+1]

        # return [left*right for left,right in zip(l,r)]

        # 动态规划+空间优化
        n = len(a)
        # tmp存每个位置左边的乘积
        l = [1] * n
        for i in range(1, n):
            l[i] = a[i - 1] * l[i - 1]
        tmp = 1
        for i in range(n - 1, -1, -1):
            l[i] *= tmp
            tmp *= a[i]
        return l




