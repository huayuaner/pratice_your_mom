# 给定一个字符串 s 和一个整数 k 。你可以从 s 的前 k 个字母中选择一个，并把它加到字符串的末尾。
#
# 返回 在应用上述步骤的任意数量的移动后，字典上最小的字符串 。
#
#  
#
# 示例 1：
#
# 输入：s = "cba", k = 1
# 输出："acb"
# 解释：
# 在第一步中，我们将第一个字符（“c”）移动到最后，获得字符串 “bac”。
# 在第二步中，我们将第一个字符（“b”）移动到最后，获得最终结果 “acb”。
# 示例 2：
#
# 输入：s = "baaca", k = 3
# 输出："aaabc"
# 解释：
# 在第一步中，我们将第一个字符（“b”）移动到最后，获得字符串 “aacab”。
# 在第二步中，我们将第三个字符（“c”）移动到最后，获得最终结果 “aaabc”。
#
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        n = len(s)
        # if k>=n:
        #     return ''.join(sorted(s))
        # s_list = list(s)
        # ans = s_list.copy()
        # for _ in range(n):
        #     idx = s_list.index(max(s_list[:k]))
        #     s_list.append(s_list.pop(idx))
        #     if s_list < ans:
        #         ans = s_list.copy()
        # return ''.join(ans)

        if k != 1:
            return ''.join(sorted(s))
        # s_list = list(s)
        ans = min(s[i:] + s[:i] for i in range(n))
        return ''.join(ans)


