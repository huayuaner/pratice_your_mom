# 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。
#
# 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
# 返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。
#
#  
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：[0,1]
# 解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
# 示例 2：
#
# 输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# 输出：[0,2,1,3]
# 解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
# 因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
# 示例 3：
#
# 输入：numCourses = 1, prerequisites = []
# 输出：[0]
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # if not prerequisites:
        #     return list(range(numCourses))
        # # seen = set()
        # # 单向的
        # grid = [set() for _ in range(numCourses)]

        # for a,b in prerequisites:
        #     # print(a,b,grid)
        #     grid[a].add(b)
        # # 我需要把b的内容全部学完才能学a
        # # print(set([1,2,3]) in set([1,2,3,4]))
        # def bfs(course):
        #     # pq = deque([course])
        #     seen = set([course])
        #     l = [course]
        #     while 1:
        #         flag = False
        #         for i in range(numCourses):
        #             if grid[i].issubset(seen) and i not in seen:
        #                 flag = True
        #                 seen.add(i)
        #                 l.append(i)
        #                 if len(seen) == numCourses:
        #                     return l
        #         if flag == False:
        #             return []
        # for i in range(numCourses):
        #     if not grid[i]:
        #         if (tmp:=bfs(i)):
        #             return tmp
        # return []

        # bfs
        # 拓扑排序
        # grid = [[] for _ in range(numCourses)]
        # # 每个节点的入度
        # node_in_deg = [0]*numCourses
        # ans = []
        # for a,b in prerequisites:
        #     # 节点b的下面的节点 a
        #     grid[b].append(a)
        #     # 节点 a入度 +1
        #     node_in_deg[a] += 1
        # # print(node_in_deg)
        # pq = deque([node for node in range(numCourses) if node_in_deg[node] == 0])
        # # print(pq)
        # while pq:
        #     node = pq.popleft()
        #     ans.append(node)
        #     # 删除入度
        #     for nex in grid[node]:
        #         # print(nex)
        #         node_in_deg[nex] -= 1
        #         if node_in_deg[nex] == 0:
        #             pq.append(nex)
        # # print(ans)
        # if len(ans) != numCourses:
        #     ans.clear()
        # return ans

        # dfs
        # 拓扑排序
        grid = [[] for _ in range(numCourses)]
        # 每个节点的入度
        # 0 未访问 1 访问中 2 访问完成
        visited = [0] * numCourses
        # 是否有环
        valid = False
        ans = []
        for a, b in prerequisites:
            # 节点b的下面的节点 a
            grid[b].append(a)

        def dfs(b):
            nonlocal valid
            visited[b] = 1
            for a in grid[b]:
                if visited[a] == 0:
                    # visited[a] = 1
                    dfs(a)
                    # 如果在递归中出现了环
                    if valid:
                        return
                # 有环
                elif visited[a] == 1:
                    valid = True
                    return
            visited[b] = 2
            ans.append(b)

        for i in range(numCourses):
            if not valid and visited[i] == 0:
                dfs(i)
                # print(i)
                # print(visited, ans)
        return ans[::-1] if len(ans) == numCourses else []





