# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
#
# 你需要按照以下要求，给这些孩子分发糖果：
#
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
#
#  
#
# 示例 1：
#
# 输入：ratings = [1,0,2]
# 输出：5
# 解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
# 示例 2：
#
# 输入：ratings = [1,2,2]
# 输出：4
# 解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 单调增栈
        # n = len(ratings)
        # ans1 = [0]*n
        # ans2 = [0]*n
        # for i, r in enumerate(ratings):
        #     if i == 0:
        #         ans1[i] = 1
        #         continue
        #     if r > ratings[i-1]:
        #         ans1[i] = ans1[i-1] + 1
        #     else:
        #         ans1[i] = 1
        #     # print(ans)
        # for i, r in enumerate(reversed(ratings)):
        #     if i == 0:
        #         ans2[n-1-i] = 1
        #         continue
        #     if r > ratings[n-i]:
        #         ans2[n-1-i] = ans2[n-i] + 1
        #     else:
        #         ans2[n-1-i] = 1

        # return sum([max(ans1[i],ans2[i]) for i in range(n)])
        n = len(ratings)
        ret = 1
        # 递增程度，递减长度，前一个孩子拿到的糖果数量
        inc, dec, pre = 1, 0, 1
        for i in range(1, n):
            # 当当前孩子评分大于等于前一个孩子的评分
            if ratings[i] >= ratings[i - 1]:
                # 递减清空
                dec = 0
                # 更新pre
                # 与前一个相同可以置1
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                # 更新答案
                ret += pre
                # 更新递增长度
                inc = pre
            else:
                # 更新递减长度
                dec += 1
                # 满足左规则
                # 因为当递减大于递增长度时，处于递增最后一个孩子需要纳入递减，原因在于在序列[1,2,3,2,1,0]，3位置的孩子应该分到4个糖果，而不是3个
                if dec == inc:
                    dec += 1
                ret += dec
                # 更新pre
                pre = 1

        return ret
