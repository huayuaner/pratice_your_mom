# 你和一群强盗准备打劫银行。给你一个下标从 0 开始的整数数组 security ，其中 security[i] 是第 i 天执勤警卫的数量。日子从 0 开始编号。同时给你一个整数 time 。
#
# 如果第 i 天满足以下所有条件，我们称它为一个适合打劫银行的日子：
#
# 第 i 天前和后都分别至少有 time 天。
# 第 i 天前连续 time 天警卫数目都是非递增的。
# 第 i 天后连续 time 天警卫数目都是非递减的。
# 更正式的，第 i 天是一个合适打劫银行的日子当且仅当：security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].
#
# 请你返回一个数组，包含 所有 适合打劫银行的日子（下标从 0 开始）。返回的日子可以 任意 顺序排列。
#
#  
#
# 示例 1：
#
# 输入：security = [5,3,3,3,5,6,2], time = 2
# 输出：[2,3]
# 解释：
# 第 2 天，我们有 security[0] >= security[1] >= security[2] <= security[3] <= security[4] 。
# 第 3 天，我们有 security[1] >= security[2] >= security[3] <= security[4] <= security[5] 。
# 没有其他日子符合这个条件，所以日子 2 和 3 是适合打劫银行的日子。
# 示例 2：
#
# 输入：security = [1,1,1,1,1], time = 0
# 输出：[0,1,2,3,4]
# 解释：
# 因为 time 等于 0 ，所以每一天都是适合打劫银行的日子，所以返回每一天。
# 示例 3：
#
# 输入：security = [1,2,3,4,5,6], time = 2
# 输出：[]
# 解释：
# 没有任何一天的前 2 天警卫数目是非递增的。
# 所以没有适合打劫银行的日子，返回空数组。
# 示例 4：
#
# 输入：security = [1], time = 5
# 输出：[]
# 解释：
# 没有日子前面和后面有 5 天时间。
# 所以没有适合打劫银行的日子，返回空数组。
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # 模拟暴力-超时
        # def check(pos, time):
        #     left,right = pos, pos
        #     i = 0
        #     while i < time:
        #         if left > 0 :
        #             if security[left-1] >= security[left]:
        #                 left -= 1
        #             else:
        #                 return False
        #         if right < len(security)-1 :
        #             if security[right+1] >= security[right]:
        #                 right += 1
        #             else:
        #                 return False
        #         i += 1
        #     return True
        # if time > len(security):
        #     return []
        # ans = []
        # n = len(security)
        # for i in range(time, n-time):
        #     if check(i,time):
        #         ans.append(i)
        # return ans

        # 单调栈
        # 单调递减栈
        # if time == 0:
        #     return [num for num in range(len(security))]
        # if time > len(security)//2:
        #     return []
        # stack = []
        # cnt = 0
        # tmp = set()
        # ans = []
        # n = len(security)
        # for i,cop in enumerate(security):
        #     while stack and cop > security[stack[-1]]:
        #         stack.pop()
        #         cnt = 0
        #     cnt += (1 if stack and stack[-1] == i-1 else 0)
        #     stack.append(i)
        #     if cnt == time:
        #         tmp.add(i)
        #         cnt -= 1
        # stack.clear()
        # cnt = 0
        # for i,cop in enumerate(reversed(security)):
        #     #print(i,cop)
        #     while stack and cop > security[stack[-1]]:
        #         #print(cop,security[stack[-1]])
        #         a = stack.pop()
        #         #print(a)
        #         cnt = 0
        #     cnt += (1 if stack and stack[-1] == n-i else 0)
        #     #print(stack,i)
        #     stack.append(n-i-1)
        #     #print(stack)
        #     if cnt == time:
        #         if n-i-1 in tmp:
        #             ans.append(n-i-1)
        #         cnt -= 1
        #     #print(stack)
        # return ans

        # 动态规划
        # if time == 0:
        #     return [num for num in range(len(security))]
        # if time > len(security)//2:
        #     return []
        # n = len(security)
        # left = [0] * n
        # right = [0] * n
        # for i in range(n):
        #     if i>0 and security[i] <= security[i-1]:
        #         left[i] = left[i-1] + 1
        #     #print(n-i-1)
        #     if i>0 and security[n-i-1] <= security[n-i]:
        #         right[n-i-1] = right[n-i] + 1
        # #print(left,right)
        # return [idx for idx in range(time, n-time) if left[idx]>= time and right[idx]>=time]

        # 动态规划+空间优化
        if time == 0:
            return [num for num in range(len(security))]
        if time > len(security) // 2:
            return []
        ans = []
        left, right = 0, 0
        n = len(security)
        # time是0的情况已经讨论过了
        for i in range(1, n - time):
            if security[i - 1] >= security[i]:
                left += 1
            else:
                left = 0
            if security[i + time - 1] <= security[i + time]:
                right += 1
            else:
                right = 0
            if left >= time and right >= time:
                ans.append(i)
        return ans




