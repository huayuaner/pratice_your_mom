给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。

输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]
示例 2：

输入：mat = [[1,2],[3,4]]
输出：[1,2,3,4]

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # DIRS = [(-1,1),(1,-1)]
        # dirs = [(0,1), (1,0)]
        # i,j = 0, 0
        # m, n = len(mat), len(mat[0])
        # if not m or not m:
        #     return []
        
        # ans = []
        # step = 0
        # while i < m-1 or j < n-1:
        #     # 遍历此对角线
        #     #print(i,j)
        #     while 0<=i<m and 0<=j<n:
        #         ans.append(mat[i][j])
        #         i += DIRS[step%2][0]
        #         j += DIRS[step%2][1]
                
        #     # 得到边界点
        #     i -= DIRS[step%2][0]
        #     j -= DIRS[step%2][1]
            
        #     # 进入下一对角线
        #     if j==n-1:
        #         i += 1
        #     elif i == m-1:
        #         j += 1
        #     else:
        #         i += dirs[step%2][0]
        #         j += dirs[step%2][1]


            
        #     # print(i,j,step,dirs)
        #     # i += dirs[step%2][0]
        #     # j += dirs[step%2][1]
        #     #print(i,j)

        #     step += 1
        # #print(i,j)
        # #print(ans)
        # ans.append(mat[i][j])
        # return ans


        ans = []
        m, n = len(mat), len(mat[0])
        i = 0
        while i < m+n-1:
            # i 是遍历对角线个数
            # 奇数个对角线
            # 当i不到m的时候，x1为i，y1为0；到了x1为m-1,y1为i-(m-1)
            # 偶数个同理
            x1 = i if i<m else m-1
            y1 = i-x1
            # 第1,3,5...趟
            while x1>=0 and y1<n:
                ans.append(mat[x1][y1])
                x1 -= 1
                y1 += 1
            # 下一趟
            i += 1
            # 判断是否跑完了
            if i>= m+n-1: break
            # 偶数个同理
            y2 = i if i<n else n-1
            x2 = i - y2
            # 第2,4,6...趟
            while(y2>=0 and x2<m):
                ans.append(mat[x2][y2])
                x2 += 1
                y2 -= 1 
            i += 1
            
        return ans 


            




