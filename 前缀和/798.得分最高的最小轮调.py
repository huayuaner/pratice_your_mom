# 给你一个数组 nums，我们可以将它按一个非负整数 k 进行轮调，这样可以使数组变为 [nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]] 的形式。此后，任何值小于或等于其索引的项都可以记作一分。
#
# 例如，数组为 nums = [2,4,1,3,0]，我们按 k = 2 进行轮调后，它将变成 [1,3,0,2,4]。这将记为 3 分，因为 1 > 0 [不计分]、3 > 1 [不计分]、0 <= 2 [计 1 分]、2 <= 3 [计 1 分]，4 <= 4 [计 1 分]。
# 在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调下标 k 。如果有多个答案，返回满足条件的最小的下标 k 。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,3,1,4,0]
# 输出：3
# 解释：
# 下面列出了每个 k 的得分：
# k = 0,  nums = [2,3,1,4,0],    score 2
# k = 1,  nums = [3,1,4,0,2],    score 3
# k = 2,  nums = [1,4,0,2,3],    score 3
# k = 3,  nums = [4,0,2,3,1],    score 4
# k = 4,  nums = [0,2,3,1,4],    score 3
# 所以我们应当选择 k = 3，得分最高。
# 示例 2：
#
# 输入：nums = [1,3,0,2,4]
# 输出：0
# 解释：
# nums 无论怎么变化总是有 3 分。
# 所以我们将选择最小的 k，即 0。
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        # 预处理
        # 模拟 （超时）
        # k = 0
        # ans = 0
        # cnt = 0
        # for idx,num in enumerate(nums):
        #     if num<=idx:
        #         cnt += 1
        # n = len(nums)
        # for k in range(1,n):
        #     tmp = 0
        #     for i in range(k, k+n):
        #         if nums[i%n]<= i-k:
        #             tmp += 1
        #     if tmp > cnt:
        #         cnt = tmp
        #         ans = k
        # return ans

        # 先看看每个数在那几个k能得分，最后选分最高的
        n = len(nums)
        cnt = [0]*n
        for idx,num in enumerate(nums):
            if idx < num:
                # 用前缀和替代
                # for i in range(num, n):
                #     cnt[n+idx-i] += 1
                cnt[idx+1] += 1
                if (pos:=n+idx-num)<n-1:
                    cnt[pos+1] -= 1
            else:
                # for i in range(idx,num-1, -1):
                #     cnt[idx-i] += 1
                cnt[0] += 1
                if idx-num < n-1:
                    cnt[idx-num+1] -= 1
                # for i in range(idx+1, n):
                #     cnt[i] += 1
                if idx+1<n:
                    cnt[idx+1] += 1

        max_ = cnt[0]
        ans = 0
        for i in range(n):
            if i==0:continue
            cnt[i] = cnt[i] + cnt[i-1]
            if cnt[i]>max_:
                max_=cnt[i]
                ans = i
        return ans

