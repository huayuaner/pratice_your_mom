# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
#
#  
#
# 示例 1：
#
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
# 示例 2:
#
# 输入: nums = [1,2,3,4], k = 3
# 输出: false

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # n = len(nums)
        # nums.sort()
        # if (tmp:=sum(nums))%k!=0:
        #     return False
        # target = tmp//k
        # if target < nums[-1]:
        #     return False
        # while nums and target == nums[-1]:
        #     nums.pop()
        #     k -= 1
        # cnts = [0] * k
        # def dfs(nums, cnts):
        #     if not nums:
        #         return True
        #     val = nums.pop()
        #     for i in range(k):
        #         if cnts[i] + val <= target:
        #             cnts[i] += val
        #             if dfs(nums,cnts):
        #                 nums.append(val)
        #                 return True
        #             cnts[i] -= val
        #             if cnts[i] == 0:
        #                 break
        #     nums.append(val)
        #     return False
        # return dfs(nums,cnts)

        n = len(nums)
        nums.sort()
        if (total:=sum(nums))%k!=0:
            return False
        target = total//k
        if target < nums[-1]:
            return False
        # 表示nums选择的情况
        m = 1<<n
        # dp[i]表示分成子集的情况，也是所有子集的和
        dp = [-1]*m
        dp[0] = 0
        for i in range(m):
            # 当前状态不可达
            if dp[i] < 0:
                continue
            for j in range(n):
                # nums从小到大排序，当前不行，后面都不行
                if nums[j] + dp[i]%target > target:
                    break
                # 第j个num没被选择
                if i & (1<<j) == 0:
                    next_state =  i ^ (1<<j)
                    # 可达，不用更新
                    if dp[next_state] > 0:
                        continue
                    dp[next_state] = dp[i] + nums[j]

                if dp[-1] == total:
                    return True
        return False