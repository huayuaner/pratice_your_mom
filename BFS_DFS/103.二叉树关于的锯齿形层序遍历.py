# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
# 示例 2：
#
# 输入：root = [1]
# 输出：[[1]]
# 示例 3：
#
# 输入：root = []
# 输出：[]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        depth = -1
        pq = [root]
        while pq:
            cur_size = len(pq)
            depth += 1
            tmp = []
            for i in range(cur_size):
                node = pq.pop(0)
                tmp.append(node.val)
                if node.left:
                    pq.append(node.left)
                if node.right:
                    pq.append(node.right)
            # print(depth)
            # tmp = tmp[::-1] if depth % 2 == 1 else tmp
            # reversed返回的是一个迭代器，不是一个数组
            # print(tmp)
            ans.append(tmp) if depth % 2 == 0 else ans.append(tmp[::-1])
        return ans

