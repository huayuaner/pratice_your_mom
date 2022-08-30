# 给你一个整数数组 nums 和一个整数 k。如果某个连续子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
#
# 请返回这个数组中 「优美子数组」 的数目。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,1,2,1,1], k = 3
# 输出：2
# 解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
# 示例 2：
#
# 输入：nums = [2,4,6], k = 1
# 输出：0
# 解释：数列中不包含任何奇数，所以不存在优美子数组。
# 示例 3：
#
# 输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# 输出：16
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 出现 奇数则+1
        # 当长度差等于奇数数量就是连续
        # cnt_odd = Counter()
        # cnt_odd[0] += 1
        # pre = 0
        # ans = 0
        # for num in nums:
        #     pre += (1 if num%2==1 else 0)
        #     if pre - k in cnt_odd:
        #         ans += cnt_odd[pre-k]
        #     cnt_odd[pre] += 1
        # return ans
        n = len(nums)
        # 这其实就是把Counter换成了数组
        # 有个要求
        # odd出现个数是有限的 0-n
        # 就可以缓过来
        cnt = [0]*(n+1)
        # 在空的情况下，odd为 0 的情况+1
        cnt[0] = 1
        odd = 0
        ans = 0
        for num in nums:
            odd += num%2
            if odd>=k:
                ans += cnt[odd-k]
            cnt[odd] += 1
        return ans

