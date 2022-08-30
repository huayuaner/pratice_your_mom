# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # def recur(i, j):
        #     if i>=j:
        #         return True
        #     # 找左右子树的分界点
        #     tmp = i
        #     while postorder[tmp] < postorder[j]:
        #         tmp += 1

        #     m = tmp
        #     # 这时的m是左右节点分开的地方
        #     while postorder[tmp] > postorder[j]:
        #         tmp += 1
        #     # 这时tmp应该找到了当前根节点的位置
        #     # 当前子树应该返回的信息1. 根节点是不是大于左小于右的那个 2.其左右子树是不是后序遍历
        #     return tmp == j and recur(i,m-1) and recur(m, j-1)
        # return recur(0, len(postorder)-1)

        # 辅助单调栈
        stack = []
        root = float("inf")
        # 反转后是中 右 左
        for num in reversed(postorder):
            if num > root:
                return False
            while stack and stack[-1] > num:
                root = stack.pop()
            stack.append(num)
        return True



