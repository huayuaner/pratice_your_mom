# 给你一棵二叉树的根节点 root ，请你构造一个下标从 0 开始、大小为 m x n 的字符串矩阵 res ，用以表示树的 格式化布局 。构造此格式化布局矩阵需要遵循以下规则：
#
# 树的 高度 为 height ，矩阵的行数 m 应该等于 height + 1 。
# 矩阵的列数 n 应该等于 2height+1 - 1 。
# 根节点 需要放置在 顶行 的 正中间 ，对应位置为 res[0][(n-1)/2] 。
# 对于放置在矩阵中的每个节点，设对应位置为 res[r][c] ，将其左子节点放置在 res[r+1][c-2height-r-1] ，右子节点放置在 res[r+1][c+2height-r-1] 。
# 继续这一过程，直到树中的所有节点都妥善放置。
# 任意空单元格都应该包含空字符串 "" 。
# 返回构造得到的矩阵 res 。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        # max_depth = -1
        # def get_height(root,depth):
        #     if not root:
        #         nonlocal max_depth
        #         max_depth = max(max_depth, depth)
        #         return
        #     depth += 1
        #     get_height(root.left,depth)
        #     get_height(root.right, depth)
        # get_height(root, -1)
        # m,n = max_depth+1,2**(max_depth+1)-1
        # ans = [['' for _ in range(n)] for _ in range(m)]
        # ans[0][(n-1)//2] = str(root.val)
        # def put_val(root,depth, col):
        #     if not root.left and not root.right:
        #         return
        #     depth += 1
        #     if root.left:
        #         left_col = col - 2**(max_depth - depth)
        #         ans[depth][left_col] = str(root.left.val)
        #         put_val(root.left, depth, left_col)
        #     if root.right:
        #         right_col = col + 2**(max_depth - depth)
        #         ans[depth][right_col] = str(root.right.val)
        #         put_val(root.right, depth, right_col)
        #     return
        # put_val(root, 0, (n-1)//2)
        # return ans

        # 优雅写法
        def calDepth(root):
            return max(calDepth(root.left)+1 if root.left else 0 , calDepth(root.right)+1 if root.right else 0)
        height = calDepth(root)
        m,n = height+1, 2**(height+1)-1
        ans = [[""for _ in range(n)] for _ in range(m)]
        def put_val(root,r,c):
            if not root:
                return
            ans[r][c] = str(root.val)
            put_val(root.left, r+1, c-2**(height-r-1))
            put_val(root.right, r+1, c+2**(height-r-1))
        put_val(root, 0, (n-1)//2)
        return ans

