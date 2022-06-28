# 学校打算为全体学生拍一张年度纪念照。根据要求，学生需要按照 非递减 的高度顺序排成一行。
#
# 排序后的高度情况用整数数组 expected 表示，其中 expected[i] 是预计排在这一行中第 i 位的学生的高度（下标从 0 开始）。
#
# 给你一个整数数组 heights ，表示 当前学生站位 的高度情况。heights[i] 是这一行中第 i 位学生的高度（下标从 0 开始）。
#
# 返回满足 heights[i] != expected[i] 的 下标数量 。
#
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # 直观想法
        # sorted_h = sorted(heights)
        # ans = 0
        # for i in range(len(heights)):
        #     if sorted_h[i] != heights[i]:
        #         ans += 1
        # return ans

        # 计数排序
        max_h = max(heights)
        cnts = [0] * (max_h + 1)

        for h in heights:
            cnts[h] += 1
        # print(cnts)
        ans = idx = 0
        for i in range(1, max_h + 1):
            for j in range(cnts[i]):
                if heights[idx] != i:
                    ans += 1
                idx += 1
        return ans



