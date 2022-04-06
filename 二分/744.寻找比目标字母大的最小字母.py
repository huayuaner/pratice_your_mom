# 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
#
# 在比较时，字母是依序循环出现的。举个例子：
#
# 如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
#  
#
# 示例 1：
#
# 输入: letters = ["c", "f", "j"]，target = "a"
# 输出: "c"
# 示例 2:
#
# 输入: letters = ["c","f","j"], target = "c"
# 输出: "f"
# 示例 3:
#
# 输入: letters = ["c","f","j"], target = "d"
# 输出: "f"

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 二分
        if target >= letters[-1]:
            return letters[0]
        n = len(letters)
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2
            if letters[m] <= target:
                l = m + 1
            else:
                r = m
        # print(l)
        # if letters[l] > target or l < n-1:
        #    return letters[l]
        # else:
        #     return letters[0]

        # else:
        return letters[l]

