# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#  
#
# 示例 1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2：
#
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # # dp[i][j]代表 word1前i个字符变成word2前j个字符的步骤
        # n, m = len(word1), len(word2)
        # # 一个字符串为空的情况
        # if n*m == 0:
        #     return n+m
        # dp = [[float("inf") for _ in range(m+1)] for _ in range(n+1)]
        # # word1前i个字符变空需要i步
        # for i in range(n):
        #     dp[i][0] = i
        # # 空字符变word[2]前j个字符需要j步
        # for j in range(m): 
        #     dp[0][j] = j
        # for i in range(1,n+1):
        #     for j in range(1,m+1):
        #         # 3种情况：1.dp[i-1][j]需要x步，dp[i][j]需要x+1步（删除）2.dp[i][j-1]需要x步，dp[i][j]需要x+1步（插入） 3.dp[i-1][j-1]需要x步，则需要查看剩余的那个字母是否相同，相同则为x，不同就是x+1
        #         # 取三种情况中最小的那个
        #         dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+int(word1[i-1]!=word2[j-1]))
        # return dp[n][m]

        # 空间优化
        # 由方法1可知，dp[i][j]主要和left，up和left up三个值有关
        # 这里使用1维数组存放，不断覆盖完成。left就是左边的值，up就是当前位置未被覆盖的值，left up 使用一个变量lu存
        # n, m = len(word1), len(word2)
        # dp = list(range(m+1))
        # # 有n行
        # for i in range(n):
        #     # 上一行的第一个值
        #     lu = dp[0]
        #     # 第一个值开始覆盖
        #     dp[0] += 1
        #     for j in range(m):
        #         # 从下标1开始赋值。lu为下一轮准备，变成j+1未变化之前的值
        #         dp[j+1],lu = min(dp[j]+1, dp[j+1]+1, lu+int(word1[i]!=word2[j])),dp[j+1]
        # return dp[-1]


        # dfs + 记忆化搜索
        # 表示word1前i个字符变成word2前j个字符需要的步数
        # @functools.lru_cache(len(word2)*len(word2))
        # def dfs(i,j):
        #     # 有一个值变成-1，说明一个为空了
        #     # 这里返回j+1或i+1是因为输入的是下标，对应真实长度需要+1
        #     if i == -1:
        #         return j+1
        #     if j == -1:
        #         return i+1
        #     ans = 0
        #     # if (i,j) in memo:
        #     #     return memo[(i,j)]
        #     ans = min(dfs(i-1,j)+1, dfs(i,j-1)+1, dfs(i-1,j-1)+int(word1[i]!=word2[j]))
        #     # memo[(i,j)] = ans
        #     return ans
        # # memo = dict()
        
        # return dfs(len(word1)-1, len(word2)-1)

        # bfs
        # 使用 visted集合保存访问过的位置
        # visit, q = set(), deque([(word1, word2, 0)])
        # while q:
        #     w1, w2, d = q.popleft()
        #     # 找没遍历到的位置
        #     if (w1, w2) not in visit:
        #         # 第一次两个子串相同，则返回最小操作数
        #         if w1 == w2:
        #             return d
        #         visit.add((w1, w2))
        #         # 删除w1，w2相同的部分
        #         while w1 and w2 and w1[0] == w2[0]:
        #             w1, w2= w1[1:], w2[1:]
        #         # 操作次数+1
        #         d += 1
        #         # 下面3种操作分别是：1改 2增 3删
        #         q.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d), (w1[1:], w2, d)])

        # bfs优化
        # 一层一层遍历，类似二叉树的层序遍历
        m, n = len(word1), len(word2)
        q, visited = [(0,0)], set((0,0))
        d = 0
        while True:
            
            for _ in range(len(q)):
                w1, w2 = q.pop(0)
            # 最多print出空，不会报错
                if word1[w1:] == word2[w2:]:
                    return d 
                while w1<m and w2<n and word1[w1] == word2[w2]:
                    w1 += 1
                    w2 += 1
                if w1<m and ((w1+1,w2) not in visited):
                    q.append((w1+1,w2))
                    visited.add((w1+1,w2))
                if w2<n and (w1,w2+1) not in visited:
                    q.append((w1,w2+1))
                    visited.add((w1,w2+1))
                if w1<m and w2<n and (w1+1,w2+1) not in visited:
                    q.append((w1+1,w2+1))
                    visited.add((w1+1,w2+1))
            
            d +=1



        