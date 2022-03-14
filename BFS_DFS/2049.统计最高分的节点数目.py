# 给你一棵根节点为 0 的 二叉树 ，它总共有 n 个节点，节点编号为 0 到 n - 1 。同时给你一个下标从 0 开始的整数数组 parents 表示这棵树，其中 parents[i] 是节点 i 的父节点。由于节点 0 是根，所以 parents[0] == -1 。
#
# 一个子树的 大小 为这个子树内节点的数目。每个节点都有一个与之关联的 分数 。求出某个节点分数的方法是，将这个节点和与它相连的边全部 删除 ，剩余部分是若干个 非空 子树，这个节点的 分数 为所有这些子树 大小的乘积 。
#
# 请你返回有 最高得分 节点的 数目 。
# 输入：parents = [-1,2,0,2,0]
# 输出：3
# 解释：
# - 节点 0 的分数为：3 * 1 = 3
# - 节点 1 的分数为：4 = 4
# - 节点 2 的分数为：1 * 1 * 2 = 2
# - 节点 3 的分数为：4 = 4
# - 节点 4 的分数为：4 = 4
# 最高得分为 4 ，有三个节点得分为 4 （分别是节点 1，3 和 4 ）。

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        def dfs(node):
            # 这个节点的得分
            score = 1
            # 除了该节点之外的长度，计算上面的父的score
            size = n - 1
            for s in son[node]:
                s_size = dfs(s)
                score *= s_size
                size -= s_size
            # 如果是root，size就会变成0，不是的话就是父的得分
            if size != 0:
                score *= size
            # print(score)
            nonlocal max_, ans
            if score > max_:
                max_ = score
                ans = 1
            elif score == max_:
                ans += 1
            return n - size

        # 记录所有点的子树
        n = len(parents)
        son = defaultdict(list)
        for i, p in enumerate(parents):
            son[p].append(i)
        ans = 0
        max_ = -1
        dfs(0)
        return ans




