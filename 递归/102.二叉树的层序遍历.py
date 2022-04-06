# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        tmp = []
        depth = 0
        pq = deque()
        pq.append((root, depth))
        pre = 0
        while pq:

            tree, dep = pq.popleft()
            if tree.left:
                pq.append((tree.left, dep + 1))
            if tree.right:
                pq.append((tree.right, dep + 1))
            # 如果层数相同，放入tmp中
            if dep == pre:
                tmp.append(tree.val)
                # print(tmp)
            # 如果层数不同，将tmp内容给ans并清空，更新pre值
            else:
                ans.append(tmp)
                # print(tmp, ans)
                # tmp.clear() 会把append到ans的结果也清除，浅拷贝
                tmp = []
                # print(ans)
                pre = dep
                tmp.append(tree.val)
        if tmp:
            ans.append(tmp)

        return ans












