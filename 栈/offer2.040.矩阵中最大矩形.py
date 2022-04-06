# 给定一个由 0 和 1 组成的矩阵 matrix ，找出只包含 1 的最大矩形，并返回其面积。
#
# 注意：此题 matrix 输入格式为一维 01 字符串数组。

# 输入：matrix = ["10100","10111","11111","10010"]
# 输出：6
# 解释：最大矩形如上图所示。
# 示例 2：
#
# 输入：matrix = []
# 输出：0
# 示例 3：
#
# 输入：matrix = ["0"]
# 输出：0


class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
        def largestRectangleArea(heights):
            stack = [-1]
            ans = 0
            n = len(heights)
            for i in range(n):
                while stack[-1]!=-1 and heights[stack[-1]] >= heights[i]:
                    idx = stack.pop()
                    ans = max(ans, (i-stack[-1]-1)*heights[idx])
                stack.append(i)
            while stack[-1]!=-1:
                idx = stack.pop()
                ans = max(ans, (n-stack[-1]-1)*heights[idx])
            return ans
        if not matrix or not matrix[0]:
            return 0
        m,n = len(matrix), len(matrix[0])
        heights = [0]*n
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] =='1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            tmp = largestRectangleArea(heights)
            # print(heights,tmp)

            ans = max(ans,tmp)
        return ans