# 给你一个下标从 0 开始的正整数数组 nums 和一个正整数 k 。
#
# 如果满足下述条件，则数对 (num1, num2) 是 优质数对 ：
#
# num1 和 num2 都 在数组 nums 中存在。
# num1 OR num2 和 num1 AND num2 的二进制表示中值为 1 的位数之和大于等于 k ，其中 OR 是按位 或 操作，而 AND 是按位 与 操作。
# 返回 不同 优质数对的数目。
#
# 如果 a != c 或者 b != d ，则认为 (a, b) 和 (c, d) 是不同的两个数对。例如，(1, 2) 和 (2, 1) 不同。
#
# 注意：如果 num1 在数组中至少出现 一次 ，则满足 num1 == num2 的数对 (num1, num2) 也可以是优质数对。
from collections import Counter
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        # 推理可得nums1 and nums2 + nums1 or nums2 相当于nums1中1的数量 + nums2中1的数量
        # cnts = Counter(x.bit_count() for x in set(nums))
        # ans = 0
        # for cnt1,ccnt1 in cnts.items():
        #     for cnt2,ccnt2 in cnts.items():
        #         if cnt1 + cnt2 >= k:
        #             ans += ccnt1 * ccnt2
        # return ans

        # 后缀和优化
        # 2^30次方 > 10**9，1的数量最多29个
        # cnts 记录每一个1的个数的出现次数
        cnts = [0] * 30
        for num in set(nums):
            cnts[num.bit_count()] += 1
        # print(cnts[0])
        # if k>30:k=30
        tot = sum(cnts[k:])
        ans = 0
        for i in range(30):
            ans += cnts[i] * tot
            if 0<=k - i - 1<30:
                tot += cnts[k - i - 1]
        return ans
