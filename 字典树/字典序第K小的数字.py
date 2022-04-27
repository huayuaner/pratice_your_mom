# 给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字。
#
#  
#
# 示例 1:
#
# 输入: n = 13, k = 2
# 输出: 10
# 解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
# 示例 2:
#
# 输入: n = 1, k = 1
# 输出: 1

# class Trie:
#     def __init__(self, k):
#         self.isEnd = False
#         self.children = [None] * 10
#         self.ans = ""
#         self.k = k
#     def insert(self, num):
#         node = self
#         for c in str(num):
#             idx = ord(c) - ord('0')
#             if not node.children[idx]:
#                 node.children[idx] = Trie(self.k)
#             node = node.children[idx]
#         node.isEnd = True
#     def search(self, node, s):
#         # print(k,node,s)
#         if self.k==0:
#             # print(s)
#             if self.ans =="":
#                 self.ans = ''.join(s)
#             return

#         if node == None:
#             return
#         for i in range(10):

#             if node.children[i]!=None:
#                 s.append(str(i))
#                 if node.children[i].isEnd:
#                    self.k -= 1
#                 self.search(node.children[i], s)
#                 s.pop()


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # 直接使用字典树 超时
        # if n == k:
        #     return n-1

        # t = Trie(k)
        # for i in range(1,n+1):
        #     t.insert(i)
        # t.search(t, [])
        # # print(t.search(k, t, []))
        # return int(t.ans)

        # 使用字典树思想
        # dfs + bfs

        # dfs 在小于n的情况下搜索以l开头之后所有的值的数量
        # l, r= 1, 1 => l, r = 10, 19 => l, r = 100, 199...
        # 这个l,r的设计很厉害
        def dfs(l, r):
            return 0 if l > n else min(n, r) - l + 1 + dfs(l * 10, r * 10 + 9)

        cur = 1
        # 从1开始往下数，所以k-1
        k -= 1
        while k:
            # 搜索以cur开头之后所有的值的数量
            cnt = dfs(cur, cur)
            # 如果该点下的数量小过k，说明第k小的数字不在该前缀下
            # 换成下一个前缀
            if cnt <= k:
                k -= cnt
                cur += 1
            # 如果该点下的数量大过k，说明第k小的数字在前缀cur其中
            else:
                k -= 1
                # 寻找前缀长度+1的最小前缀
                cur *= 10
        return cur