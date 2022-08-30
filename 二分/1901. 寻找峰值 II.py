# 一个 2D 网格中的 峰值 是指那些 严格大于 其相邻格子(上、下、左、右)的元素。
#
# 给你一个 从 0 开始编号 的 m x n 矩阵 mat ，其中任意两个相邻格子的值都 不相同 。找出 任意一个 峰值 mat[i][j] 并 返回其位置 [i,j] 。
#
# 你可以假设整个矩阵周边环绕着一圈值为 -1 的格子。
#
# 要求必须写出时间复杂度为 O(m log(n)) 或 O(n log(m)) 的算法
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def get_val_idx(nums):
            max_val, max_idx = nums[0], 0
            for i in range(1, len(nums)):
                if nums[i] > max_val:
                    max_val = nums[i]
                    max_idx = i
            return max_val, max_idx
        l,r = 0, len(mat)-1
        while l<=r:
            m = l + (r-l)//2
            # print(m,l,r)
            max_val, max_idx = get_val_idx(mat[m])
            if m + 1 < len(mat) and mat[m + 1][max_idx] > max_val:
                l = m + 1
            elif m > 0 and mat[m-1][max_idx] > max_val:
                r = m
            else:
                return [m,max_idx]
            # print(l,r)