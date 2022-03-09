# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
# 叶子节点 是指没有子节点的节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        # dfs
        def helper(root, target):
            if not root:
                return
            path.append(root.val)
            target -= root.val
            if not root.left and not root.right and target == 0:
                # print(path)
                # path[:]得到了一个有别于path的新list，但与path值完全相同，如果放入path，后续path的改变会导致其变化
                ans.append(path[:])
            # print(target)
            helper(root.left, target)
            # print(target)
            helper(root.right, target)
            # 当当前节点的左右都搜索完之后将这个节点从path中删除
            path.pop()

        ans = []
        path = []
        helper(root, target)
        return ans

        # def helper(root, tmp):
        #     if not root:
        #         return
        #     tmp.append(root.val)
        #     if not root.left and not root.right and sum(tmp) == target:
        #         ans.append(tmp)
        #     # tmp[:]可以得到一个区别与tmp但与tmp相同的list，所以成立，如果用tmp，left递归的结果也会保存进去，导致错误
        #     helper(root.left, tmp)
        #     helper(root.right, tmp)
        #     # 回溯过程中删除左右都搜索过的节点值
        #     tmp.pop()
        #
        # ans = []
        # helper(root, [])
        # return ans

        # bfs
        # if not root:
        #     return []
        # ans = []
        # pq = [(root,root.val, [root.val])]
        # while pq:
        #     node, sum_, tmp = pq.pop(0)
        #     #print(tmp,node)
        #     if not node.left and not node.right and sum_ == target:
        #         ans.append(tmp[:])
        #     # 直接使用tmp会因为tmp的改变导致后面的改变
        #     a, b = tmp[:], tmp[:]
        #     if node.left:
        #         a.append(node.left.val)
        #         #print(a)
        #         pq.append((node.left, sum_ + node.left.val, a))
        #         tmp.pop()
        #     if node.right:
        #         b.append(node.right.val)
        #         pq.append((node.right, sum_ + node.right.val, b))

        # return ans

