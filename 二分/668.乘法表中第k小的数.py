# 几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？
#
# 给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。
#
# 例 1：
#
# 输入: m = 3, n = 3, k = 5
# 输出: 3
# 解释:
# 乘法表:
# 1	2	3
# 2	4	6
# 3	6	9
#
# 第5小的数字是 3 (1, 2, 2, 3, 3).
# 例 2：
#
# 输入: m = 2, n = 3, k = 6
# 输出: 6
# 解释:
# 乘法表:
# 1	2	3
# 2	4	6
#
# 第6小的数字是 6 (1, 2, 2, 3, 4, 6).

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # m, n = len(matrix), len(matrix[0])

        # def check(mid):
        #     i, j = 1, n
        #     cnt = 0
        #     while i <= m and j > 0:
        #         if i*j > mid:
        #             j -= 1
        #         else:
        #             # print(i,j)
        #             i += 1
        #             cnt += j
        #     # print(cnt)
        #     return cnt >= k

        # left, right = 1, m*n
        # while left < right:
        #     mid = left + (right - left) // 2
        #     # print(left, right, mid)
        #     if check(mid):
        #         right = mid
        #     else:
        #         left = mid + 1
        # return left
        # return bisect_left(range(m * n), k, key=lambda x: x // n * n + sum(x // i for i in range(x // n + 1, m + 1)))


