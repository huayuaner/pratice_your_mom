# 你打算利用空闲时间来做兼职工作赚些零花钱。
#
# 这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。
#
# 给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。
#
# 注意，时间上出现重叠的 2 份工作不能同时进行。
#
# 如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = list(zip(startTime, endTime, profit))
        # for i in range(len(startTime)):
        #     arr.append((startTime[i],endTime[i], profit[i]))
        arr.insert(0, [0, 0, 0])
        arr.sort(key=lambda x: x[1])
        # arr.insert(0,[0,0,0])

        n = len(arr)
        # print(arr)
        dp = [0] * n

        def find(l, r, start):
            while l < r:
                m = l + (r - l + 1) // 2
                if arr[m][1] <= start:
                    l = m
                else:
                    r = m - 1
            return l

        for i in range(1, n):
            pre_idx = find(0, i - 1, arr[i][0])
            # print(pre_idx)
            dp[i] = max(dp[i - 1], dp[pre_idx] + arr[i][2])
        # print(dp)
        return dp[-1]

