# 图像平滑器 是大小为 3 x 3 的过滤器，用于对图像的每个单元格平滑处理，平滑处理后单元格的值为该单元格的平均灰度。
#
# 每个单元格的  平均灰度 定义为：该单元格自身及其周围的 8 个单元格的平均值，结果需向下取整。（即，需要计算蓝色平滑器中 9 个单元格的平均值）。
#
# 如果一个单元格周围存在单元格缺失的情况，则计算平均灰度时不考虑缺失的单元格（即，需要计算红色平滑器中 4 个单元格的平均值）。
#

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # m, n = len(img), len(img[0])
        # ans = [[None for _ in range(n)]for _ in range(m)]
        # for x in range(m):
        #     for y in range(n):
        #         tmp = img[x][y]
        #         cnt = 1
        #         for nx,ny in [(x-1,y+1),(x,y+1),(x+1,y+1),(x-1,y),(x+1,y),(x-1,y-1),(x,y-1),(x+1,y-1)]:
        #             if 0<=nx<m and 0<=ny<n:
        #                 tmp += img[nx][ny]
        #                 cnt += 1
        #         ans[x][y] = tmp // cnt
        # return ans

        # 二维前缀和
        m, n = len(img), len(img[0])
        # sum[i][j]表示 以img[i-1][j-1]为右下角，[0][0]为左上角的方块的和
        sum_ = [[0 for _ in range(n+1)]for _ in range(m+1)]
        ans = [[None for _ in range(n)]for _ in range(m)]
        for i in range(1,m+1):
            for j in range(1, n+1):
                # 大方形为左，上两个方形之和 - 重叠部分 + 右下角小方形
                sum_[i][j] = sum_[i-1][j] + sum_[i][j-1] - sum_[i-1][j-1] + img[i-1][j-1]
        for i in range(m):
            for j in range(n):
                left = max(j-1, 0)
                right = min(j+1,n-1)
                top = max(i-1, 0)
                bottom = min(i+1, m-1)
                cnt = (right-left+1)*(bottom-top+1)
                # 大方形 - 左，上两个方形 + 重叠部分
                total = sum_[bottom+1][right+1] - sum_[top][right+1] - sum_[bottom+1][left] + sum_[top][left]
                ans[i][j] = total // cnt
        return ans