在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

 if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        # 从左下或右上开始，每次可以失效最多个数的位置
        i, j = 0, n-1
        while 0<=i<m and 0<=j<n:
            # 该点左边失效
            if matrix[i][j] < target:
                i += 1
            # 该点下方失效
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False