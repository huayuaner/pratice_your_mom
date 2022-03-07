给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        total = m*n
        ans = []
        # 记录遍历时能到达的边界
        top = 0
        bottom = m-1
        left = 0
        right = n-1
        while total>0:
            for i in range(left,right+1):
                #print(top,i)
                if total <= 0 :break
                ans.append(matrix[top][i])
                total -= 1
            top += 1
            for i in range(top,bottom+1):
                #print(i,right)
                if total <= 0 :break
                ans.append(matrix[i][right])
                total -= 1
            right -= 1
            for i in range(right,left-1,-1):
                if total <= 0 :break
                ans.append(matrix[bottom][i])
                total -= 1
            bottom -= 1
            for i in range(bottom, top-1, -1):
                if total <= 0 :break
                ans.append(matrix[i][left])
                total -= 1
            left += 1
            print(top,bottom,left,right)
        return ans


             
