# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
#  
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # self.ans = TreeNode(0)
        # def helper(root, p ,q):
        #     if not root:
        #         return False
        #     # lson代表左孩子有没有p或q
        #     lson = helper(root.left, p, q)
        #     rson = helper(root.right, p, q)
        #     # 有两种情况当前root是p,q的最大公共祖先
        #     # 1.当该节点左右节点都存在p或q 2.当该节点的值等于r或q 并且rson和lson存在p和q
        #     if (lson and rson) or ((root.val==p.val or root.val==q.val) and (lson or rson)):
        #         self.ans = root
        #     # 当左、右孩子为True或root为p或q返回True
        #     return lson or rson or root.val==p.val or root.val==q.val
        # helper(root, p, q)
        # return self.ans

        self.map  = dict()
        self.set = set()
        def dfs(root):
            # 这里key是.val而value是TreeNode
            if root.left:
                self.map[root.left.val] = root
                dfs(root.left)
            if root.right:
                self.map[root.right.val] = root
                dfs(root.right)
        dfs(root)
        while p :
            # 将p的父节点的值放入集合中（包括p本身）
            self.set.add(p.val)
            # p更新成它的父节点
            p = self.map[p.val] if p.val in self.map else None
        while q:
            # 查看q的值是否在集合中
            if q.val in self.set:
                return q 
            # 将q更新成其父节点
            q = self.map[q.val] 


            
        



