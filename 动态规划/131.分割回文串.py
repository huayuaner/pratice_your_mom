# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
#
# 回文串 是正着读和反着读都一样的字符串。
#
#  
#
# 示例 1：
#
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 示例 2：
#
# 输入：s = "a"
# 输出：[["a"]]
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def check(strs):
            return True if strs == strs[::-1] else False

        def dfs(lis, pos):
            if pos >= n:
                nonlocal ans
                # print(lis)
                # 注意深浅拷贝
                ans.append(lis[:])
            # 用i当作切的终点
            for i in range(pos+1, n+1):
                tmp = s[pos:i]
                if check(tmp):
                    lis.append(tmp)
                    dfs(lis, i)
                    lis.pop()
        ans = []
        dfs([], 0)
        return ans