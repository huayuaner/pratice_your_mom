# 给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。
#
# 你必须找到一个内存复杂度优于 O(n2) 的解决方案。
#
#  
#
# 示例 1：
#
# 输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# 输出：13
# 解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13
# 示例 2：
#
# 输入：matrix = [[-5]], k = 1
# 输出：-5
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 从右上开始搜
        m, n = len(matrix), len(matrix[0])

        def check(mid):
            i, j = 0, n - 1
            cnt = 0
            while i < n and j >= 0:
                if matrix[i][j] > mid:
                    j -= 1
                else:
                    i += 1
                    cnt += j + 1
            print(cnt)
            return cnt >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = left + (right - left) // 2
            print(left, right, mid)
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
