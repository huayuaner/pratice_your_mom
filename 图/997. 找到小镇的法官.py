# 小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。
#
# 如果小镇法官真的存在，那么：
#
# 小镇法官不会信任任何人。
# 每个人（除了小镇法官）都信任这位小镇法官。
# 只有一个人同时满足属性 1 和属性 2 。
# 给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。
#
# 如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 小镇法官不信任何人 -> 在trust中 ai不会出现 i
        # 每个人都信任小镇法官 -> bi中会出现 n-1 相同的数字
        # 只有一个人同时满足属性1 属性 2
        # if not trust:
        #     return n if n == 1 else -1
        # trusted = [0]*n
        # a_vis = [False]*n
        # ans = None
        # for a,b in trust:
        #     a_vis[a-1] = True
        #     trusted[b-1] += 1
        #     if trusted[b-1] == n-1:
        #         if ans == None:
        #             ans = b
        #         else:
        #             return -1
        # return ans if ans and a_vis[ans-1]==False else -1

        # 出度入度统计
        # 一个人入度为 n-1且出度为0即可
        trusted = [0]*n
        for a,b in trust:
            trusted[a-1] -= 1
            trusted[b-1] += 1
        for i in range(n):
            if trusted[i] == n-1:
                return i+1
        return -1



