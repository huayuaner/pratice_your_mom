给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        total = n*n
        step = 1
        ans = [[0 for _ in range(n)] for _ in range(n)]
        #print(ans)
        # 记录遍历时能到达的边界
        top = 0
        bottom = n-1
        left = 0
        right = n-1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                #print(top,i)
                #if step > total :break
                #print(top,i)
                ans[top][i] = step
                step += 1
               
            top += 1
            for i in range(top,bottom+1):
                #print(i,right)
                #if step > total :break
                ans[i][right] = step
                step += 1
            right -= 1
            for i in range(right,left-1,-1):
                #if step > total :break
                ans[bottom][i] = step
                step += 1
            bottom -= 1
            for i in range(bottom, top-1, -1):
                #if step > total :break
                ans[i][left] = step
                step += 1
            left += 1
        return ans